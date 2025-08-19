# HarvestPadi Demo (Django)

A demo web app showcasing:
- AI Yield Prediction (demo logic)
- AI Disease Detection (stub)
- Marketplace (buyers, investors, sellers, farmers)
- Renewable Energy Marketplace & Energy Usage Tracker
- Bilingual UI (English/Hausa)

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py loaddata          # none required
python manage.py seed_demo         # load demo data
python manage.py runserver
```

Visit http://127.0.0.1:8000

## Notes
- Yield/Disease logic are demo stubs in `aihub/ai_logic.py`.
- Hausa translations provided in `locale/ha/...`. To compile, run:
  ```bash
  django-admin compilemessages
  ```
  (You may need GNU gettext tools installed.)
- Energy usage tracker is a simple log with totals; extend as needed.
- Marketplace supports four listing types: `produce`, `input`, `investment`, `rfq`.
- Onboarding is session-based for demo only (no auth flow).
