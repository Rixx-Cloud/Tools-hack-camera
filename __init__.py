"""
Package untuk keamanan dan tools edukasi.
Gunakan secara bertanggung jawab!
"""

# Import modul agar mudah diakses dari luar
from .web_scraper import scrape_public_data
from .network_tools import check_port_status
from .image_processor import compress_image
from .encryption_tools import generate_key, encrypt_data, decrypt_data

# Versi package
__version__ = "1.0.0"

# Tentukan fungsi/modul yang akan diekspos
__all__ = [
    "scrape_public_data",
    "check_port_status",
    "compress_image",
    "generate_key",
    "encrypt_data",
    "decrypt_data",
    "__version__"
]