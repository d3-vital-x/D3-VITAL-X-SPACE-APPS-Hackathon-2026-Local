# D³ VITAL-X — Complete Data Manifest & Provenance

**Project: D³ VITAL-X Space Intelligence Platform**

**Team: D³ VITAL-X BANGLADESH**
Research **Lead: Md. Ra-bi-ul Islam**
Research Domain: Space Science, Astrophysical Data Analysis, Biomedical Signal Processing, Noise Resilience
Document Type: Data Manifest, Source Attribution & Processing Provenance
Project Status: Independent Research Prototype

---

## 1. Overview

D³ VITAL-X is an independent research prototype designed to explore a unified signal-analysis architecture across multiple scientific data domains.

The platform integrates publicly available scientific data and derived test datasets to evaluate:

* **Scientific data ingestion and inspection.**
* **FITS and CSV data handling.**
* **Data quality control.**
* **Biomedical signal analysis.**
* **Noise-resilience evaluation.**
* **Statistical feature extraction.**
* **Exploratory anomaly analysis.**
* **Data provenance and reproducibility.**

The current research data inventory includes **NASA/MAST JWST** NIRSpec science products, PhysioNet MIT-BIH ECG benchmark records, recorded noise signals, and a project-generated biomedical stress-test dataset.

Data integrity principle: Original source data, extracted science products, and project-generated datasets are documented separately. No derived dataset is represented as an original NASA observation.

---

## 2. Complete Data Inventory — 10 Logical Entries

The following inventory groups related files into logical data assets. It does not imply that the repository contains or hosts the original files.

No.| Data Asset| Source| Format| Reported Size| Availability
|:---|:---|:---|:---|:---|:---|
01| MAST Archive 2233| NASA / MAST| ZIP| 26.6 MB| Downloaded
02| JWST NIRSpec Calibrated Science Product| NASA / MAST| FITS| To be verified| Google Drive link
03| MAST Archive 2230| NASA / MAST| ZIP| To be verified| Downloaded
04| JWST NIRSpec S2D Science Product| NASA / MAST| FITS| 3.31 MB| Google Drive link
05| MIT-BIH ECG Record 100| PhysioNet| DAT, HEA, ATR| ~1.86 MB| Downloaded and inspected
06| Baseline Wander Noise Record (BW)| PhysioNet| DAT, HEA| ~1.86 MB| Downloaded and inspected
07| Electrode Motion Noise Record (EM)| PhysioNet| DAT, HEA| ~1.86 MB| Downloaded and inspected
08| Muscle / EMG Noise Record (MA)| PhysioNet| DAT, HEA| ~1.86 MB| Downloaded and inspected
09| Biomedical Signal Stress-Test Dataset V1| Derived from PhysioNet| CSV| 8.71 MB| Generated and verified
10| ECG Annotations & Dataset Metadata| Project-generated from source data| CSV, JSON| To be verified| Generated

Inventory clarification: Entries 01–04 represent two **NASA/MAST** archive packages and their corresponding JWST FITS science products. Entries 05–08 represent the nine downloaded PhysioNet raw files grouped by record. Entry 09 is the derived **8.71 MB CSV** dataset. Entry 10 represents its supporting annotation and metadata files.

---

## 3. NASA / MAST / JWST Data

**3.1 MAST Archive — Observation Package 2233**

Original archive filename:

`"MAST_2026-11-03T2233.zip"`

**Reported archive size: 26.6 MB**

**Source: NASA** Mikulski Archive for Space Telescopes **(MAST)**

**Official archive:** [NASA Mikulski Archive for Space Telescopes (MAST)](https://mast.stsci.edu/)

This archive was downloaded from MAST and used in the JWST NIRSpec science-data workflow.

**Associated FITS science product:**

`"jw03855-o002_t112-s000000014_nirspec_f290lp-g395h-s1600a1_cal.fits"`

**FITS file access:**

[**Open JWST NIRSpec CAL FITS — Google Drive**](https://drive.google.com/file/d/1jfnxxzdfTfFzIazIoQroNdLgdbMfS8Xy/view?usp=drivesdk)

The **FITS** product is used for scientific-data inspection and astrophysical data-processing workflows.

## 3.2 MAST Archive — Observation Package 2230

**Original archive filename:**

`"MAST_2026-11-03T2230.zip"`

**Archive size:** To be verified.

**Source: NASA** Mikulski Archive for Space Telescopes **(MAST)**

**Associated FITS science product:**

`"jw03855-o002_t112-s000000014_nirspec_f290lp-g395h-s1600a1_s2d.fits"`

**Previously reported FITS size:** 3.31 MB.

**FITS file access:**

[**Open JWST NIRSpec S2D FITS — Google Drive**](https://drive.google.com/file/d/1whuggiitqIpU4wHCEwqvxAHtx3z6zrjx/view?usp=drivesdk)


This product is included in the platform's FITS inspection and astrophysical data-analysis workflow.

---

## 3.3 NASA Data Processing Scope

The two **MAST** archive packages were downloaded separately and associated with their respective **JWST NIRSpec FITS** science products.

**The platform's intended inspection and processing tasks include:**

* **FITS file and HDU inspection.**
* **Header and metadata extraction.**
* **Data dimensions and data-type** inspection.
* **Science-product routing.**
* **Data-quality checks.**
* **Exploratory statistical and signal analysis.**

The exact **FITS** header metadata, observation provenance, and archive-to-product relationship should be retained for reproducibility.

Important distinction: These are **JWST** science-data products, not astronaut physiological data and not necessarily spacecraft telemetry. Their scientific interpretation depends on the actual **FITS** contents and observation metadata.

---

## 4. Biomedical Data Sources — PhysioNet

The biomedical validation workflow uses two publicly available PhysioNet databases.

## 4.1 MIT-BIH Arrhythmia Database

**Official source:** [PhysioNet MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/)

**Selected record:** "100"

**Downloaded files:**

Filename| Description| Reported size
---|---|---
"100.dat"| Binary ECG signal| 1,904.3 KB
"100.hea"| Signal header and metadata| 0.14 KB
"100.atr"| Expert beat annotations| 4.45 KB

**Inspection results:**

**Parameter| Verified value**
---|---
Sampling frequency| 360 Hz
Number of channels| 2
Channel names| MLII, V5
Signal samples| 650,000
Duration| 1,805.56 seconds
Signal units| mV
Total annotations| 2,274
Signal shape| 650,000 × 2

This record is used as a public human-*ECG* benchmark for exploratory biomedical signal-processing and validation tasks.

---

## 4.2 MIT-BIH Noise Stress Test Database

**Official source:** [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/)

Three recorded noise records were downloaded.

**A. Baseline Wander (BW)**

* `"bw.dat"`
* `"bw.hea"`

**B. Electrode Motion (EM)**

* `"em.dat"`
* `"em.hea"`

**C. Muscle / EMG Noise (MA)**

* `"ma.dat"`
* `"ma.hea"`

**Inspection results:**

**Parameter| Verified value**
---|---
Sampling frequency| 360 Hz
Channels per record| 2
Samples per record| 650,000
Duration per record| 1,805.56 seconds
Signal units| mV

The three noise records are used for controlled noise-resilience experiments.

**Source attribution:** The original PhysioNet datasets must be credited, and their applicable license terms must be respected.

---

## 5. Project-Generated Biomedical Dataset

## 5.1 Dataset Identification

**Filename:**
`"D3_VITAL_X_BIOMEDICAL_SIGNAL_STRESS_TEST_V1.csv"`

**File size:** 8.71 MB

**Google Drive access:**
[Open Biomedical Signal Stress-Test Dataset V1 — Google Drive](https://drive.google.com/file/d/1nBIRT9bvRYHd8nO5UozsuELTdMRLGb7W/view?usp=drivesdk)

**Source lineage:**

* **MIT-BIH Arrhythmia Database — ECG Record 100.**
* **MIT-BIH Noise Stress Test Database — BW, EM, and MA recorded noise.**
* **Project-controlled noise mixing and CSV generation.**

---

## 5.2 Dataset Generation Results

Parameter| Verified result
---|---
Output file size| 8.71 MB
Rows| 80,000
Columns| 10
Sampling frequency| 360 Hz
Duration| 222.22 seconds
Target SNR| 10 dB
Measured SNR| 10 dB across all six noisy channels
Noise conditions| 3
ECG leads| 2
Generation status| Successful

---

## 5.3 Dataset Signal Structure

**The CSV contains:**

- **Sample index.**
- **Time in seconds.**
- **Clean MLII ECG signal.**
- **Clean V5 ECG signal.**
- **MLII with Baseline Wander noise.**
- **VV5 with Baseline Wander noise.**
- **MLII with Electrode Motion noise.**
- **V5 with Electrode Motion noise.**
- **MLII with Muscle / EMG noise.**
- **V5 with Muscle / EMG noise.**

---

## 5.4 Noise Conditions

Noise type| MLII measured SNR| V5 measured SNR
---|---|---
Baseline Wander| 10.0 dB| 10.0 dB
Electrode Motion| 10.0 dB| 10.0 dB
Muscle / EMG| 10.0 dB| 10.0 dB

All six measured aggregate SNR values matched the 10 dB target.

The noisy channels were generated independently. The three noise types were not combined into a single mixed-noise condition.

Scientific limitation: The mapping of noise channel 0 to MLII and noise channel 1 to V5 is an experimental computational pairing. It does not reproduce actual electrode placement or a clinically calibrated acquisition setup.

---

## 6. Astronaut Medical Data Availability and Research Limitation

A central objective of the biomedical validation workflow was to evaluate the platform using astronaut-related physiological research data.

However, for this prototype, we did not obtain a verified, openly accessible raw astronaut-specific medical waveform dataset suitable for the intended ECG noise-resilience experiment.

Therefore, we constructed a derived biomedical stress-test dataset using publicly available human-ECG benchmark data and separately recorded noise signals.

**The dataset-generation process involved:**

1. **Downloading MIT-BIH ECG Record 100.**
2. **Downloading three recorded noise datasets: BW, EM, and MA.**
3. **Inspecting sampling rates, channel dimensions, signal units, and sample counts.**
4. **Applying controlled noise mixing at a target SNR of 10 dB.**
5. **Exporting an 80,000-row, 10-column CSV.**
6. **Measuring the resulting SNR and exporting supporting annotations and metadata.**

**This dataset is not real astronaut medical data.**

It is not a measured astronaut health record, and it is not a validated astronaut physiology simulation.

It is a derived human-**ECG** research stress-test dataset used to evaluate the platform's data-ingestion, signal-processing, and noise-analysis capabilities.

No medical diagnosis, astronaut health assessment, clinical decision, or flight-safety certification is claimed.

---

## 7. Data Processing and Validation Architecture

### Biomedical Workflow

<pre>
PhysioNet / MIT-BIH ECG Record 100
                |
                v
       Raw ECG Inspection
                |
                v
 MIT-BIH Recorded Noise (BW / EM / MA)
                |
                v
   Sampling & Dimension Checks
                |
                v
       Controlled SNR Mixing
                |
                v
      Derived Biomedical CSV
                |
                v
           CSV Adapter
                |
                v
       Unified Data Layer
                |
                v
      Data Quality Control
                |
                v
    Feature / Signal Analysis
                |
                v
      Visualization & Export
                |
                v
          Human Review
</pre>

### Space Science Workflow

<pre>
NASA / MAST Archive Packages
                |
                v
       JWST NIRSpec Products
                |
                v
          FITS Inspection
                |
                v
       Header / HDU Analysis
                |
                v
       Data Quality Checks
                |
                v
      Science Product Routing
                |
                v
    Exploratory Data Analysis
                |
                v
      Visualization & Export
</pre>

The biomedical and astrophysical workflows use separate source-specific ingestion and validation pathways.

---

## 8. Data Storage and Access Policy

**D³ VITAL-X BANGLADESH** does not store the large original datasets directly inside the public **GitHub** repository.

**Instead:**

- **Source datasets are obtained from their original scientific archives.**
- **Selected processed files are made accessible through Google Drive links.**
- **The GitHub repository contains documentation, source references, processing information, and validation summaries.**
- **Original source files are kept separate from derived project outputs.**

**External Data Links**

Dataset| Access
---|---
JWST NIRSpec CAL FITS| "Google Drive" (https://drive.google.com/file/d/1jfnxxzdfTfFfIazIoQroNdLgdbMfS8Xy/view?usp=drivesdk)
JWST NIRSpec S2D FITS| "Google Drive" (https://drive.google.com/file/d/1whuggiitqIpU4wHCEwqvxAHtx3z6zrjx/view?usp=drivesdk)
Biomedical Stress-Test CSV| "Google Drive" (https://drive.google.com/file/d/1nBIRT9bvRYHd8nO5UozsuELTdMRLGb7W/view?usp=drivesdk)
MIT-BIH Arrhythmia Database| "PhysioNet" (https://physionet.org/content/mitdb/1.0.0/)
MIT-BIH Noise Stress Test Database| "PhysioNet" (https://physionet.org/content/nstdb/1.0.0/)
NASA MAST Archive| "MAST Portal" (https://mast.stsci.edu/)

**Access note:** Google Drive files must have appropriate sharing permissions enabled for intended reviewers. The original **MAST ZIP** archives are documented by filename; separate public Drive links for those **ZIP** files have not been supplied in this manifest.

---

## 9. Data Integrity and Reproducibility

**For reproducible research, the following metadata should be retained for each data asset:**

- **Original filename.**
- **Source archive or database.**
- **Official source URL.**
- **Download date.**
- **File size in bytes.**
- **File format.**
- **SHA-256 checksum.**
- **Observation identifier, where applicable.**
- **Sampling frequency, where applicable.**
- **Processing parameters.**
- **Validation status.**
- **Derived-file lineage.**

Raw source files should remain unchanged.

Derived files should be stored separately and clearly identified as processed or generated outputs.

Checksums should be calculated from the actual files. No checksum is claimed in this report until it has been computed and recorded.

---

## 10. Validation Status

Validation item| Status
---|---
MIT-BIH ECG raw files downloaded| Successful
MIT-BIH noise files downloaded| Successful
All 9 PhysioNet raw files verified| Successful
ECG record sampling and dimensions inspected| Successful
BW / EM / MA sampling and dimensions inspected| Successful
ECG annotations inspected| Successful
8.71 MB derived CSV generated| Successful
80,000 rows and 10 columns verified| Successful
Six aggregate SNR measurements verified| Successful
Annotation CSV exported| Successful
Dataset metadata JSON exported| Successful
JWST CAL FITS available through Drive link| Link supplied; independent file inspection pending
JWST S2D FITS available through Drive link| Link supplied; independent file inspection pending
MAST archive contents fully inventoried| Pending
SHA-256 checksums generated| Pending
Dashboard-level biomedical validation| Pending

---

## 11. Research Scope and Limitations

**The data assets in this manifest support research-prototype testing in:**

- **Space-science FITS ingestion and inspection.**
- **Biomedical CSV ingestion.**
- **Signal quality assessment.**
- **Noise-resilience evaluation.**
- **Entropy and variance analysis.**
- **Statistical feature extraction.**
- **Exploratory anomaly analysis.**
- **Data provenance and reproducibility.**

The platform's analytical outputs are exploratory computational indicators.

They must not be interpreted as confirmed astrophysical discoveries, medical diagnoses, astronaut health assessments, or certified spacecraft safety decisions.

All source-specific attribution, access conditions, and licensing requirements must be respected.

---

## 12. Final Statement

**D³ VITAL-X BANGLADESH** combines **NASA/MAST JWST** science products, publicly available PhysioNet biomedical benchmark signals, recorded noise datasets, and a transparently derived biomedical stress-test **CSV.**

The project distinguishes original scientific data from derived test data and documents their respective sources, processing pathways, and limitations.

The current biomedical stress-test dataset was generated because a verified, openly accessible astronaut-specific raw medical waveform dataset was not obtained for this prototype.

This approach allows the team to test its signal-analysis architecture without misrepresenting public human-ECG benchmark data as astronaut medical records.

**Driven by Logic, Not by Degrees.**

## D³ VITAL-X BANGLADESH

**Transform the World, Illuminate the Future.**
