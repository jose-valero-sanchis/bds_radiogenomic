import os
import numpy as np
import SimpleITK as sitk

def load_lesion_3d(lesion_file):
    with open(lesion_file, 'rb') as f:
        # Tamaño total del archivo
        f.seek(0,2)
        file_size = f.tell()
        f.seek(0)

        # Leemos 6 valores de 2 bytes => (3,2)
        rg_raw = np.fromfile(f, dtype=np.uint16, count=6)
        rg = rg_raw.reshape((3, 2))

        # Ordenamos cada par para evitar que (start,end) se inviertan
        rg_sorted = np.sort(rg, axis=1)

        # Dimensiones
        sz = rg_sorted[:, 1] - rg_sorted[:, 0] + 1
        n_voxels = np.prod(sz)

        # Verificación de tamaño
        remaining_bytes = file_size - 12  # 12 bytes de cabecera
        if n_voxels != remaining_bytes:
            print(f"WARNING: {lesion_file} dimensionada a {n_voxels} voxels, "
                  f"pero quedan {remaining_bytes} bytes en el archivo.")
        
        # Lectura de máscara
        mask_flat = np.fromfile(f, dtype=np.int8, count=n_voxels)
        if mask_flat.size < n_voxels:
            print(f"WARNING: {lesion_file} - Se han leído menos voxeles de los esperados.")

        # Reshape (ny, nx, nz)
        mask_3d = mask_flat.reshape(sz[0], sz[1], sz[2])
    
    # Devolvemos la máscara y la matriz de coordenadas (ya ordenadas)
    return mask_3d, rg_sorted

def convert_les_to_sitk(lesion_file, output_file=None):
    """
    Carga la máscara .les y la convierte en SimpleITK.
    Si se especifica output_file, escribe .nii.gz
    """
    mask_3d, rg = load_lesion_3d(lesion_file)
    sitk_mask = sitk.GetImageFromArray(mask_3d)
    
    if output_file:
        sitk.WriteImage(sitk_mask, output_file)
    
    return sitk_mask, rg

if __name__ == "__main__":
    data_path = "../data/"
    base_path = os.path.join(data_path, 'TCGA_Segmented_Lesions_UofC')
    
    les_files = sorted(os.listdir(base_path))
    les_files = [f for f in les_files if f.lower().endswith('.les')]

    for f in les_files:
        lesion_file = os.path.join(base_path, f)
        output_file = os.path.join(
            base_path,
            os.path.splitext(f)[0] + '_mask.nii.gz'
        )
        print(f"Convirtiendo: {lesion_file} -> {output_file}")
        
        mask_sitk, rg = convert_les_to_sitk(lesion_file, output_file)