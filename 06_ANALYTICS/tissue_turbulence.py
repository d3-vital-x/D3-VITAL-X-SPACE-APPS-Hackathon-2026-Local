import numpy as np


def evaluate_tissue_turbulence(
    signal_index,
    entropy_delta_series,
    variance_series,
    threshold_score=2.13,
    entropy_drop_threshold=-2.5,
    variance_threshold=7.0,
):
    """
    Exploratory localized signal-anomaly screening.

    entropy_delta_series:
        Change in entropy (current - previous), not raw entropy.

    variance_series:
        Variance or energy feature computed using a consistent
        preprocessing and measurement scale.

    This function does not diagnose disease or estimate
    a Lyapunov exponent.
    """

    entropy = np.asarray(
        entropy_delta_series, dtype=np.float64
    ).reshape(-1)

    variance = np.asarray(
        variance_series, dtype=np.float64
    ).reshape(-1)

    if entropy.size != variance.size:
        raise ValueError(
            "Entropy and variance arrays must have equal lengths."
        )

    if signal_index is not None:
        indices = list(signal_index)
        if len(indices) != entropy.size:
            raise ValueError(
                "signal_index length must match feature arrays."
            )
    else:
        indices = list(range(entropy.size))

    detected_anomalies = []

    for idx, (delta_h, var) in enumerate(
        zip(entropy, variance)
    ):
        if not np.isfinite(delta_h) or not np.isfinite(var):
            continue

        entropy_drop = delta_h <= entropy_drop_threshold
        variance_spike = var >= variance_threshold

        # Score: 1 if both configured conditions are satisfied.
        anomaly_score = float(
            entropy_drop and variance_spike
        )

        if anomaly_score >= threshold_score:
            detected_anomalies.append({
                "index": indices[idx],
                "entropy_delta": round(float(delta_h), 4),
                "variance_energy": round(float(var), 4),
                "anomaly_score": anomaly_score,
                "status_flag": (
                    "Localized Signal Anomaly Detected"
                ),
                "lyapunov_status": "not_estimated",
            })

    if detected_anomalies:
        return {
            "inspection_result": "ANOMALY_INDEX_FOUND",
            "details": detected_anomalies,
            "note": (
                "Exploratory localized signal anomaly. "
                "Independent validation and expert review required. "
                "This result is not a clinical diagnosis."
            ),
        }

    return {
        "inspection_result": "NO_ANOMALY_DETECTED",
        "details": [],
        "note": (
            "No anomaly detected under the configured thresholds. "
            "This does not establish that the tissue or signal is normal."
        ),
    }
