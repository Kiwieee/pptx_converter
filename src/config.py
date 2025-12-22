"""
Configuration management for team project
Reads API keys from environment variables or secure config file
"""
import os
from pathlib import Path

# Try to load .env file
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def get_api_key(key_name: str, config_file: str = None) -> str:
    """
    Get API key with fallback hierarchy:
    1. Environment variable
    2. .env file (loaded by dotenv)
    3. Team config file (shared securely, not in Git)

    Args:
        key_name: Name of the environment variable (e.g., "GOOGLE_API_KEY")
        config_file: Optional path to shared config file

    Returns:
        API key string

    Raises:
        ValueError: If key not found anywhere
    """
    # Check environment variable first
    api_key = os.environ.get(key_name)
    if api_key:
        return api_key

    # Check team config file (if provided)
    if config_file:
        config_path = Path(config_file)
        if config_path.exists():
            with open(config_path, 'r') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        if '=' in line:
                            var_name, var_value = line.strip().split('=', 1)
                            if var_name.strip() == key_name:
                                return var_value.strip()

    # Not found anywhere
    raise ValueError(
        f"❌ {key_name} not found!\n\n"
        f"For team members:\n"
        f"  1. Ask your team lead for the shared .env file\n"
        f"  2. Place it in the project root directory\n"
        f"  3. Make sure it's named '.env' (not .env.txt)\n\n"
        f"Or set it as environment variable:\n"
        f"  Windows: set {key_name}=your_key_here\n"
        f"  Linux/Mac: export {key_name}=your_key_here"
    )


# Easy access functions
def get_google_api_key() -> str:
    """Get Google Gemini API key"""
    return get_api_key("GOOGLE_API_KEY")


def get_deepl_api_key() -> str:
    """Get DeepL API key (optional)"""
    try:
        return get_api_key("DEEPL_API_KEY")
    except ValueError:
        # DeepL is optional, return None if not found
        return None


# For debugging
if __name__ == "__main__":
    print("🔍 Checking API keys...\n")

    try:
        google_key = get_google_api_key()
        print(f"✅ Google Gemini: Found ({google_key[:10]}...)")
    except ValueError as e:
        print(f"❌ Google Gemini: {e}")

    try:
        deepl_key = get_deepl_api_key()
        if deepl_key:
            print(f"✅ DeepL: Found ({deepl_key[:10]}...)")
        else:
            print("⚠️  DeepL: Not found (will use free translation)")
    except ValueError:
        print("⚠️  DeepL: Not found (will use free translation)")