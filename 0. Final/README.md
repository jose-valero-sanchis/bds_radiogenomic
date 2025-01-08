# Breast Cancer Subtype Classification Project

This project leverages machine learning to predict breast cancer molecular subtypes using a combination of radiomic, clinical, and genomic features. Below is an overview of the project structure and detailed descriptions of the contents within the `code` directory.

## Summary of Notebooks

### `0_data/`
- **`get_target_class.ipynb`**: Selects the `Pam50.Call` variable, which represents the molecular subtype of cancer. Only samples present in all three datasets (radiomic, clinical, and multigenic assays) are retained to ensure consistency and completeness for the analysis.
- **`plot_image_segmentation.ipynb`**: Displays the MRI images with segmentation overlays to verify the correctness of tumor annotations and segmentations.

### `1_exploratory_analysis/`
- **`clinical_data.ipynb`**: Analyzes clinical variables such as age at diagnosis, tumor stage, and hormone receptor status. Visualizations include histograms, box plots, and correlation matrices to explore relationships.
- **`multigenic_assays.ipynb`**: Explores genomic features from assays like Oncotype DX and MammaPrint. Key metrics include recurrence scores and proliferation-related gene expressions.
- **`radiomic_features.ipynb`**: Performs an in-depth analysis of radiomic features, focusing on descriptors of tumor shape, texture, and enhancement dynamics.

### `2_modeling/`
- **`all.ipynb`**: A comprehensive model that combines radiomic, clinical, and genomic data.
- **`mutigenic.ipynb`**: A model trained using only multigenic assay features.
- **`only_clinical.ipynb`**: A model trained using only clinical variables, such as age and tumor stage.
- **`only_multigenic.ipynb`**: Uses only genomic data for subtype prediction.
- **`radiomic_features+clinical_data(optimistic).ipynb`**: Combines radiomic features and clinical variables, including hormone receptor status.
- **`radiomic_features+clinical_data(pessimistic).ipynb`**: Similar to the previous model but excludes hormone receptor data to reduce overly optimistic results.
- **`radiomic_features.ipynb`**: A baseline model using only radiomic features from MRI images.

## Key Findings
The inclusion of clinical variables, especially hormone receptor status, significantly boosts performance. However, when combining all data types (`all.ipynb`), performance did not surpass the radiomic + clinical (optimistic) model due to potential feature redundancy.

## References
For details, refer to `bds_report.pdf`, which contains a comprehensive discussion of methodology, evaluation metrics, and future directions.