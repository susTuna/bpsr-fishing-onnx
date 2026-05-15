import os
import urllib.request

from ok import Logger

logger = Logger.get_logger(__name__)

GITHUB_REPO = "susTuna/bpsr-fishing-onnx"
MODEL_FILENAME = "bpsr_splash.onnx"
PRIMARY_URL = f"https://github.com/{GITHUB_REPO}/releases/latest/download/{MODEL_FILENAME}"


def _report_progress(block_num, block_size, total_size):
    if total_size <= 0:
        return
    pct = min(block_num * block_size * 100 // total_size, 100)
    print(f"\r  Downloading model ... {pct}%", end="", flush=True)

def ensure_model(weights_path):
    """
    Make sure weights_path exists. If not, download it from the latest
    GitHub release. Raises RuntimeError on failure.
    """
    if os.path.exists(weights_path):
        return

    os.makedirs(os.path.dirname(weights_path), exist_ok=True)
    logger.info(f"Model not found at '{weights_path}'. Downloading from GitHub ...")

    try:
        urllib.request.urlretrieve(PRIMARY_URL, weights_path, reporthook=_report_progress)
        print()
        logger.info(f"Model downloaded to '{weights_path}'.")
    except Exception as exc:
        if os.path.exists(weights_path):
            os.remove(weights_path)
        raise RuntimeError(
            f"Failed to download model from '{PRIMARY_URL}': {exc}\n"
            "Please download it manually from:\n"
            f"  https://github.com/{GITHUB_REPO}/releases/latest"
        ) from exc