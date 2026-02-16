import plistlib
from pathlib import Path


def get_version() -> str:
    """Extract version from version.plist."""
    vplist_path = Path(__file__).parent / "version.plist"
    with vplist_path.open("rb") as f:
        plist = plistlib.load(f)
    return str(plist["Version"] or "Unknown")


__version__: str = get_version()
