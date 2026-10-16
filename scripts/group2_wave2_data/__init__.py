"""Wave 2 Japanese & Korean models aggregator."""
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
if str(DATA_DIR) not in sys.path:
    sys.path.insert(0, str(DATA_DIR))

from toyota_models import PRADO_MODEL, KLUGER_MODEL, TOYOTA_86_MODEL, SUPRA_MODEL, CELICA_MODEL
from toyota_models_part2 import AURION_MODEL, CROWN_MODEL, HIACE_MODEL, YARIS_MODEL
from mazda_models import MX5_MODEL, CX5_MODEL, RX3_808_MODEL, MAZDA_626_6_MODEL
from mitsubishi_models import EVO_MODEL, OUTLANDER_MODEL, MITSUBISHI_380_MODEL, STARION_CORDIA_MODEL
from nissan_models import NAVARA_MODEL, XTRAIL_MODEL, PULSAR_MODEL, Z_CAR_MODEL
from subaru_models import FORESTER_MODEL, LIBERTY_OUTBACK_MODEL
from honda_suzuki_isuzu_models import CIVIC_MODEL, JIMNY_SIERRA_MODEL, ISUZU_DMAX_MODEL

ALL_WAVE2_MODELS = [
    # Toyota (9)
    PRADO_MODEL,
    KLUGER_MODEL,
    TOYOTA_86_MODEL,
    SUPRA_MODEL,
    CELICA_MODEL,
    AURION_MODEL,
    CROWN_MODEL,
    HIACE_MODEL,
    YARIS_MODEL,
    # Mazda (4)
    MX5_MODEL,
    CX5_MODEL,
    RX3_808_MODEL,
    MAZDA_626_6_MODEL,
    # Mitsubishi (4)
    EVO_MODEL,
    OUTLANDER_MODEL,
    MITSUBISHI_380_MODEL,
    STARION_CORDIA_MODEL,
    # Nissan (4)
    NAVARA_MODEL,
    XTRAIL_MODEL,
    PULSAR_MODEL,
    Z_CAR_MODEL,
    # Subaru (2)
    FORESTER_MODEL,
    LIBERTY_OUTBACK_MODEL,
    # Honda, Suzuki, Isuzu (3)
    CIVIC_MODEL,
    JIMNY_SIERRA_MODEL,
    ISUZU_DMAX_MODEL,
]
