
# **D³ VITAL-X — Biomedical Signal Screening**

**Project: D³ VITAL-X Space Intelligence Platform**  
**Module:** Biomedical Signal Analysis  
**Analysis Pipeline:** v11 Exploratory Signal Analysis  
**Screening Module:** CELL 04 — Candidate Fluctuation Region Screening  
**Status:** Exploratory Analysis Completed  
**Team: D³ VITAL-X BANGLADESH**

---

## **1. Overview**

This documentation presents an exploratory multichannel ECG signal-analysis workflow developed within the **D³ VITAL-X** research platform.

The objective was to examine localized signal fluctuations across two ECG leads under different controlled noise conditions using statistical signal features, entropy–variance relationships, residual analysis, and robust candidate-region screening.

**The workflow includes:**

- Biomedical data ingestion and integrity checks
- Time-axis and sampling-rate verification
- Clean-versus-noisy signal characterization
- Window-based entropy and variance analysis
- First-difference RMS analysis
- Clean-reference residual assessment
- Entropy–variance coupling analysis
- Robust candidate fluctuation-region screening

**The analysis is intended for computational signal exploration and methodological development. It does not establish clinical abnormalities or confirmed physical turbulence.**

## **2. Dataset Description**

**Dataset filename:**

`D3_VITAL_X_BIOMEDICAL_SIGNAL_STRESS_TEST_V1.csv`

| Property | Value |
|---|---|
| Dataset rows | 80,000 |
| Total columns | 10 |
| ECG signal tracks | 8 |
| ECG leads | 2 |
| Noise categories | 3 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Infinite numerical values | 0 |
| Sampling rate | ~359.999712 Hz |
| Recording duration | 222.219444 seconds |
| Sampling interval | ~0.00277778 seconds |

### **Signal Inventory**

**The dataset contains two ECG leads:**

- MLII
- V5

**Each lead includes:**

1. Clean reference signal
2. Baseline Wander noise variant
3. Electromagnetic noise variant
4. Motion Artifact noise variant

### **Signal Columns**

**MLII:**

- `ecg_mlII_clean_mV`
- `ecg_mlII_bw_noisy_mV`
- `ecg_mlII_em_noisy_mV`
- `ecg_mlII_ma_noisy_mV`

**V5:**

- `ecg_v5_clean_mV`
- `ecg_v5_bw_noisy_mV`
- `ecg_v5_em_noisy_mV`
- `ecg_v5_ma_noisy_mV`

**Additional columns:**

- `sample_index`
- `time_seconds`

The dataset provides clean reference tracks and corresponding noise variants for controlled comparative signal analysis.

**Dataset provenance and licensing should be verified against the original source before redistribution.**

## **3. Data Integrity and Provenance**

The original uploaded dataset was recorded with the following SHA-256 checksum:

`1ee30d573c292a7b4d438cee93e97ed5f785a6c69ae5d0e090fc4c95b1a89206`

**The localized-analysis input representation produced the following SHA-256 identifier:**

`dd855317d94ee1fcbb91d57724ba270df8660bd1a99ebe358c047558ac44b547`

**These hashes identify different representations:**

- The first hash identifies the original CSV file bytes.
- The second identifies the numerical analysis input representation used in the localized analysis workflow.

**They should not be treated as interchangeable file checksums.**

**The ingestion report recorded:**

- 80,000 rows
- 10 columns
- Zero missing cells
- Zero duplicate rows
- Zero infinite numerical values

The characterization stage confirmed a strictly increasing time axis and continuous sample indexing.

## **4. Analysis Configuration**

**The localized analysis used the following configuration:**

| Parameter | Value |
|---|---|
| Window size | 200 samples |
| Step size | 50 samples |
| Window duration | ~0.555556 seconds |
| Step duration | ~0.138889 seconds |
| Histogram bins | 32 |
| Leads analyzed | 2 |
| Noise categories | 3 |
| Windows per lead–noise combination | 1,597 |
| Total screening windows | 9,582 |

**Shared histogram edges were used within each lead's signal tracks to maintain consistent histogram boundaries during window-based entropy comparisons.**

## **5. Analytical Methodology**

### **5.1 Signal Characterization**

**The initial characterization stage examined:**

- Signal mean and standard deviation
- Variance and RMS
- Minimum and maximum amplitude
- Peak-to-peak amplitude
- Clean-versus-noisy correlation
- Residual signal statistics
- Inter-signal correlation

### **5.2 Localized Entropy Analysis**

The signal was divided into overlapping windows.

A fixed set of histogram boundaries was used within each lead to estimate window-based Shannon entropy.

\[
H=-\sum_i p_i\log_2(p_i)
\]

The resulting entropy values were used to investigate changes in the distribution of signal amplitudes across successive windows.

### **5.3 Variance Analysis**

Window-based signal variance was calculated to characterize localized amplitude dispersion.

Variance differences were examined across clean and noisy signal variants.

### **5.4 Residual Analysis**

Noisy signals were compared with their corresponding clean reference signals.

Residual measurements were used to characterize differences between the reference and noise-containing tracks.

### **5.5 First-Difference RMS**

First-difference RMS was used to examine localized changes in residual signal behavior.

**This metric provides a measure of short-term residual variation; it is not a direct measurement of physical turbulence.**

### **5.6 Entropy–Variance Coupling**

Correlation between localized entropy and variance features was calculated separately for each lead and signal type.

**The observed correlations were:**

| Lead | Signal Type | Correlation |
|---|---|---:|
| MLII | Clean | 0.762346 |
| MLII | Baseline Wander | 0.732786 |
| MLII | Electromagnetic | 0.687310 |
| MLII | Motion Artifact | 0.702611 |
| V5 | Clean | 0.592178 |
| V5 | Baseline Wander | 0.584137 |
| V5 | Electromagnetic | 0.578620 |
| V5 | Motion Artifact | 0.571366 |

These values describe feature-level statistical relationships within the analyzed dataset. They do not establish causation or a universal physical relationship.

## **6. Candidate Fluctuation-Region Screening**

**The final screening stage used the metric:**

`residual_difference_rms_mV`

A robust threshold was calculated independently for each lead–noise combination.

**The primary threshold rule was:**

\[
T=\operatorname{Median}(x)+3(1.4826)\operatorname{MAD}(x)
\]

**Where:**

- Median is the median of the selected metric.
- MAD is the median absolute deviation.
- 1.4826 is the normal-consistency scaling factor.
- 3 is the selected screening multiplier.

If MAD was effectively zero, the implementation used a 99th-percentile fallback.

Consecutive threshold-exceeding windows were merged into candidate regions.

**The resulting regions are algorithmically identified screening outputs.**

**They are not confirmed turbulence events or independent physiological events.**

## **7. Final Screening Results**

**The final screening identified:**

**75 candidate fluctuation regions across six lead–noise combinations.**

### **7.1 Screening Summary**

| Lead | Noise Category | Total Windows | Flagged Windows | Candidate Regions |
|---|---|---:|---:|---:|
| MLII | Baseline Wander | 1,597 | 94 | 18 |
| MLII | Electromagnetic | 1,597 | 18 | 6 |
| MLII | Motion Artifact | 1,597 | 30 | 11 |
| V5 | Baseline Wander | 1,597 | 60 | 12 |
| V5 | Electromagnetic | 1,597 | 23 | 8 |
| V5 | Motion Artifact | 1,597 | 57 | 20 |
| **Total** | | **9,582** | **282** | **75** |

### **7.2 Candidate Window Fractions**

| Lead | Noise Category | Candidate Window Fraction |
|---|---|---:|
| MLII | Baseline Wander | 5.8860% |
| MLII | Electromagnetic | 1.1271% |
| MLII | Motion Artifact | 1.8785% |
| V5 | Baseline Wander | 3.7570% |
| V5 | Electromagnetic | 1.4402% |
| V5 | Motion Artifact | 3.5692% |

**The overall flagged-window fraction was approximately 2.943% of the 9,582 screening windows.**

### **7.3 Maximum Residual Difference RMS**

| Lead | Noise Category | Maximum Metric |
|---|---|---:|
| MLII | Baseline Wander | 0.009144 mV |
| MLII | Electromagnetic | 0.008102 mV |
| MLII | Motion Artifact | 0.036630 mV |
| V5 | Baseline Wander | 0.003953 mV |
| V5 | Electromagnetic | 0.006359 mV |
| V5 | Motion Artifact | 0.036847 mV |

**The highest observed value occurred in the V5 Motion Artifact condition:**

`0.036847 mV`

**The MLII Motion Artifact condition recorded:**

`0.036630 mV`

These are observed metric maxima, not clinical severity measurements.

## **8. Interpretation**

The exploratory analysis identified different localized fluctuation patterns across the two ECG leads and three noise categories.

**Motion Artifact produced the highest observed maximum residual difference RMS in both leads.**

Baseline Wander produced the highest number of threshold-exceeding windows in the MLII lead and a substantial number in V5.

However, the thresholds were calculated independently for each lead–noise combination.

**Therefore, candidate-window counts and candidate-region counts must not be interpreted as direct comparisons of absolute noise severity across categories.**

The 75 candidate regions represent threshold-based computational screening results that may warrant further investigation.

**They do not establish confirmed signal turbulence, clinical abnormalities, or pathological events.**

## **9. Scientific Limitations and Responsible Interpretation**

**The following limitations apply:**

1. This workflow is an exploratory signal-analysis and screening prototype.
2. The candidate-region threshold is not clinically validated.
3. Candidate regions are not confirmed turbulence events.
4. ECG morphology, noise artifacts, and local amplitude changes can influence the extracted features.
5. Overlapping windows are correlated and are not independent observations.
6. The selected threshold does not establish sensitivity, specificity, diagnostic accuracy, or false-positive rate.
7. No independent clinical reference labels or expert-adjudicated event labels were used in this screening result.
8. White-noise, shuffled-signal, multi-seed, and other validation results must be reported separately if completed; they are not established by this report.
9. Dataset source-level provenance, acquisition protocol, and redistribution permissions require independent verification.
10. No clinical diagnosis, medical decision, astronaut health determination, or flight certification is produced.

**D³ VITAL-X does not replace medical professionals, clinical review, or validated medical monitoring systems.**

## **10. Reproducibility and Output Artifacts**

**The final screening stage generated the following outputs:**

| File | Description |
|---|---|
| `candidate_fluctuation_regions.csv` | Detailed candidate-region records |
| `candidate_screening_summary.csv` | Per-combination screening statistics |
| `D3_VITAL_X_Final_Biomedical_Report.json` | Structured final analysis report |
| `README_Biomedical_Signal_Screening.md` | Screening-stage report |

The analysis configuration, dataset identifiers, and output artifacts should be retained together to support traceability.

A reproducible notebook and any additional plots may be included when available and verified.

## **11. Research Significance**

This implementation demonstrates a modular workflow for examining multichannel ECG signal fluctuations under controlled noise conditions.

**It brings together:**

- Structured data ingestion
- Signal-quality characterization
- Localized statistical feature extraction
- Entropy–variance analysis
- Residual-based fluctuation assessment
- Robust candidate-region screening
- Structured research reporting

The work provides a foundation for further methodological validation, noise-resilience testing, and future integration into broader biomedical and space-related signal-analysis workflows.

## **12. Future Development**

**Potential next steps include:**

- Multi-seed reproducibility testing
- White-noise and shuffled-signal controls
- Sensitivity analysis across window sizes and thresholds
- Independent validation datasets
- Expert-reviewed reference annotations
- Further evaluation of false-positive behavior
- Improved visualization and report generation
- Integration with the broader D³ VITAL-X platform

**These are future validation and development objectives, not completed results of this report.**

---

# **Final Status**

**BIOMEDICAL SIGNAL SCREENING: COMPLETED**

**Candidate Regions Identified:** 75

**Lead–Noise Combinations:** 6

**Total Screening Windows:** 9,582

**Interpretation:** Exploratory Signal Fluctuation Screening Only

---

# **D³ VITAL-X BANGLADESH**

**One AI Engine. Multiple Worlds. One Signal Language.**

**Driven by Logic, Not by Degrees.**

**Transform the World, Illuminate the Future.**
