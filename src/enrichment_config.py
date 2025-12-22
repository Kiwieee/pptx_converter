"""
Enrichment Configuration Module
Defines enrichment levels and prompt templates for AI content enrichment.

Author: [Your Name]
"""

from typing import Dict, Any
from enum import Enum


class EnrichmentLevel(Enum):
    """Content enrichment levels for AI narration."""
    NONE = "none"
    MINIMAL = "minimal"
    NORMAL = "normal"
    DETAILED = "detailed"
    ACADEMIC = "academic"


# ============================================================================
# ENRICHMENT LEVEL CONFIGURATIONS
# ============================================================================

ENRICHMENT_LEVELS: Dict[str, Dict[str, Any]] = {
    "none": {
        "name": "None (No Enrichment)",
        "description": "Original text only, no additional information",
        "icon": "",
        "add_examples": False,
        "add_statistics": False,
        "add_context": False,
        "add_fun_facts": False,
        "max_extra_sentences": 0,
        "temperature": 0.3,
    },
    "minimal": {
        "name": "Minimal",
        "description": "Fluent narration, very little extra info",
        "icon": "",
        "add_examples": False,
        "add_statistics": False,
        "add_context": True,
        "add_fun_facts": False,
        "max_extra_sentences": 1,
        "temperature": 0.5,
    },
    "normal": {
        "name": "Normal",
        "description": "Some explanations and simple examples",
        "icon": "",
        "add_examples": True,
        "add_statistics": False,
        "add_context": True,
        "add_fun_facts": False,
        "max_extra_sentences": 3,
        "temperature": 0.6,
    },
    "detailed": {
        "name": "Detailed",
        "description": "Examples, statistics, and extra context",
        "icon": "",
        "add_examples": True,
        "add_statistics": True,
        "add_context": True,
        "add_fun_facts": True,
        "max_extra_sentences": 5,
        "temperature": 0.7,
    },
    "academic": {
        "name": "Academic",
        "description": "In-depth, source-referenced content",
        "icon": "",
        "add_examples": True,
        "add_statistics": True,
        "add_context": True,
        "add_fun_facts": True,
        "add_sources": True,
        "max_extra_sentences": 8,
        "temperature": 0.7,
    },
}


# ============================================================================
# PROMPT TEMPLATES FOR EACH ENRICHMENT LEVEL
# ============================================================================

ENRICHMENT_PROMPTS: Dict[str, str] = {
    "none": """
You are a presentation narrator. Convert the following slide content into natural speech.

RULES:
- Do NOT add any new information
- Do NOT add examples, statistics, or fun facts
- Just make the text flow naturally for spoken presentation
- Keep it concise and direct

Slide Content:
{slide_text}

Output the narration text only, nothing else.
""",

    "minimal": """
You are a presentation narrator. Convert the following slide content into natural, flowing speech.

RULES:
- Keep the core content unchanged
- Make it conversational and easy to follow
- You may add ONE brief transitional phrase for flow
- Do NOT add examples or statistics
- Keep it concise

Slide Content:
{slide_text}

Previous Context (for flow):
{previous_context}

Output the narration text only, nothing else.
""",

    "normal": """
You are an engaging teacher narrating a presentation slide.

TASK:
- Convert the slide content into engaging spoken narration
- Add 1-2 brief clarifying explanations where helpful
- You may include ONE simple real-world example
- Make it conversational but informative

RULES:
- Stay relevant to the topic
- Don't over-explain simple concepts
- Maximum 3 additional sentences beyond the original content

Slide Content:
{slide_text}

Previous Context:
{previous_context}

Presentation Topic:
{presentation_topic}

Output the narration text only.
""",

    "detailed": """
You are an expert educator creating rich, engaging content for a video lecture.

TASK:
- Convert the slide content into comprehensive spoken narration
- Add relevant examples from real-world applications
- Include interesting statistics or data points when relevant
- Add "Did you know?" type facts to maintain engagement
- Connect concepts to the broader topic

ENRICHMENT GUIDELINES:
- Add 2-3 relevant examples or case studies
- Include 1-2 statistics or data points if applicable
- Add context about why this matters
- Keep the tone engaging and educational

Slide Content:
{slide_text}

Previous Context:
{previous_context}

Presentation Topic:
{presentation_topic}

Output the enriched narration text only.
""",

    "academic": """
You are a university professor creating lecture content with academic depth.

TASK:
- Convert the slide content into scholarly but accessible narration
- Provide in-depth explanations with proper context
- Reference well-known theories, researchers, or studies when relevant
- Include historical context or evolution of concepts
- Connect to broader academic discourse

ACADEMIC ENRICHMENT:
- Add theoretical background where relevant
- Mention key researchers or foundational work (e.g., "As [Researcher] demonstrated in [Year]...")
- Include relevant statistics from reputable sources
- Explain implications and applications
- Note any ongoing debates or recent developments

TONE:
- Scholarly but not dry
- Accessible to students
- Intellectually stimulating

Slide Content:
{slide_text}

Previous Context:
{previous_context}

Presentation Topic:
{presentation_topic}

Output the academically enriched narration text only.
""",
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_enrichment_level_config(level: str) -> Dict[str, Any]:
    """
    Get configuration for a specific enrichment level.
    
    Args:
        level: Enrichment level key (none, minimal, normal, detailed, academic)
    
    Returns:
        Configuration dictionary for the level
    """
    return ENRICHMENT_LEVELS.get(level.lower(), ENRICHMENT_LEVELS["normal"])


def get_enrichment_prompt(level: str) -> str:
    """
    Get the prompt template for a specific enrichment level.
    
    Args:
        level: Enrichment level key
    
    Returns:
        Prompt template string
    """
    return ENRICHMENT_PROMPTS.get(level.lower(), ENRICHMENT_PROMPTS["normal"])


def get_available_levels() -> Dict[str, Dict[str, Any]]:
    """
    Get all available enrichment levels for UI display.
    
    Returns:
        Dictionary of all enrichment levels with their configurations
    """
    return ENRICHMENT_LEVELS


def format_prompt(level: str, slide_text: str, previous_context: str = "", 
                  presentation_topic: str = "") -> str:
    """
    Format the enrichment prompt with actual content.
    
    Args:
        level: Enrichment level
        slide_text: The slide content to enrich
        previous_context: Context from previous slides
        presentation_topic: Overall topic of the presentation
    
    Returns:
        Formatted prompt ready for AI
    """
    template = get_enrichment_prompt(level)
    
    return template.format(
        slide_text=slide_text,
        previous_context=previous_context if previous_context else "This is the first slide.",
        presentation_topic=presentation_topic if presentation_topic else "General presentation"
    )


# ============================================================================
# UI HELPER - Dropdown Options
# ============================================================================

def get_dropdown_options() -> list:
    """
    Get enrichment levels formatted for UI dropdown.
    
    Returns:
        List of tuples (key, display_text) for dropdown
    """
    options = []
    for key, config in ENRICHMENT_LEVELS.items():
        display = f"{config['name']} - {config['description']}"
        options.append((key, display))
    return options


# ============================================================================
# FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🔬 ENRICHMENT LEVELS")
    print("=" * 60)
    
    for key, config in ENRICHMENT_LEVELS.items():
        print(f"\n{config['icon']} {config['name']}")
        print(f"   {config['description']}")
        print(f"   Examples: {config.get('add_examples', False)}")
        print(f"   Statistics: {config.get('add_statistics', False)}")
        print(f"   Max Extra: {config.get('max_extra_sentences', 0)} sentences")
    
    print("\n" + "=" * 60)
    print("✅ Configuration loaded successfully!")
