# Visit with Us — Wellness Tourism MLOps

Dataset: `data/tourism.csv`. The positive `ProdTaken` label reflects historical purchases; the source does **not** separately label wellness-specific purchases, so predictions assume that prior purchase propensity is a useful proxy for the new product and require a wellness-specific validation campaign before production use.

## Pipeline
1. `python model_building/data_register.py` validates expected fields.
2. `python model_building/prep.py` makes 80:20 stratified train/test splits; pipeline uploads/downloads these as GitHub Actions artifacts.
3. `python model_building/train.py` tunes Random Forest and Gradient Boosting with cross-validation, logs parameters/metrics to MLflow when installed, and saves a fitted preprocessing+model pipeline and metrics.
4. `.github/workflows/pipeline.yml` runs on main pushes or manual dispatch and commits the fitted model back to main.
5. Streamlit deploy path: `deployment/app.py`; configure requirements with `deployment/requirements.txt`.

## Publish
Create your GitHub repository and push this repository's **contents** from the project package root. Actions must have read/write permissions to update the main branch; branch protection may require an alternate PR-based flow. Review run logs under Actions. Deploy with [Streamlit Community Cloud](https://share.streamlit.io/) and set entrypoint to `deployment/app.py` after workflow success. Add actual repository URL, Streamlit URL, and authentic screenshots to your notebook; these cannot be generated from local execution.

## Leakage and limits
Pitch duration, pitch satisfaction, number of follow-ups, contact method, and product pitched are intentionally removed for a pre-contact use case; identifier and export-index are also excluded. Model selection is by CV average precision, *not* test results. Metrics on historical data do not establish performance on wellness package customers; test on actual wellness campaigns before deploying to production. Respect consent and audit potential demographic bias.

## Repository layout
Upload the **contents** of this extracted folder to the repository root (not the ZIP itself). GitHub does not unpack ZIP files.
The model is included so the Streamlit app can start; rerun CI to refresh it.
