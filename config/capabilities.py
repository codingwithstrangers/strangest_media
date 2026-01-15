CAPABILITIES = {
    # -----------------------
    # YouTube Long-Form Video
    # -----------------------
    "youtube_long": {
        "content_types": {"long"},
        "privacy_modes": {"private", "unlisted", "public"},
        "features": {
            "video_upload": True,
            "set_title": True,           # Max 100 chars
            "set_description": True,     # Max 5000 bytes
            "set_tags": True,            # Max 500 chars total (not 500 tags)
            "thumbnail_upload": True,
            "playlist_management": True,
            "caption_upload_and_manage": True,
            "publishAt_scheduling": True, 
            "category_assignment": True,
            "language_assignment": True,
            "self_declared_made_for_kids": False, # REQUIRED by law/API
            "embeddable_control": True,
            "license_type": ["youtube", "creativeCommon"]
        },
        "limits": {
            "max_duration_minutes": 720,
            "max_file_size_gb": 128,      # Standard limit is 128GB (256GB is rare/verified)
            "aspect_ratios": ["16:9", "4:3", "1:1"],
            "daily_quota_cost": 1600      # Cost per upload (out of 10,000 default units)
        },
    },

    # -----------------------
    # YouTube Shorts
    # -----------------------
    "youtube_shorts": {
        "content_types": {"short"},
        "privacy_modes": {"private", "unlisted", "public"},
        "features": {
            "video_upload": True,
            "hashtag_trigger": True,      # IMPORTANT: Must include #Shorts in title/desc
            "set_title": True,
            "set_description": True,
            "set_tags": True,
            "thumbnail_upload": True,     # API allows it, but Shorts often auto-select
            "playlist_management": True,
            "category_assignment": True,
            "monetization_api_control": False, # Usually managed in Studio
            "cards_management": False,
            "end_screens": False,         # Not available for vertical < 60s
        },
        "limits": {
            "max_duration_seconds": 60,   # Strictly 60s or less
            "max_file_size_gb": 2,
            "aspect_ratios": ["9:16", "1:1"],
            "daily_quota_cost": 1600
        },
    },

  
    # -----------------------
    # Instagram Reels
    # -----------------------
    "instagram_reels": {
        "media_type": "REELS",
        "features": {
            "direct_publish": True,      # Requires Instagram Business/Creator account
            "set_caption": True,         # Max 2,200 characters
            "set_hashtags": True,        # Max 30 hashtags
            "custom_cover_upload": True, # Aspect ratio 9:16 recommended
            "tag_users": True,           # Support for collaborator tags
            "location_tagging": True,
            "share_to_feed": True,       # Can toggle visibility on main grid
            "audio_rename": True         # Set "Original Audio" name via API
        },
        "limits": {
            "max_duration_seconds": 180, # Expanded to 3 minutes in 2025/2026
            "min_duration_seconds": 3,
            "max_file_size_mb": 300,     # Graph API limit for direct uploads
            "aspect_ratio": "9:16",      # Strictly vertical (1080x1920)
            "frame_rate": "23-60 FPS",
            "daily_upload_limit": 25,    # Standard API rate limit for media publishing
        },
    },

    # -----------------------
    # Instagram Stories
    # -----------------------
    "instagram_stories": {
        "media_type": "STORIES",
        "features": {
            "video_upload": True,
            "image_upload": True,        # Supports JPG/PNG
            "set_caption": False,        # API does NOT support text overlays/captions yet
            "link_stickers": False,      # Limited API support (usually manual only)
            "mention_users": False,      # Generally requires manual interaction in app
            "is_ad_eligible": True,
        },
        "limits": {
            "max_duration_seconds": 60,  # Stories now support 60s clips without splitting
            "max_file_size_mb": 100,     # Lower limit than Reels
            "aspect_ratio": "9:16",
            "lifespan_hours": 24,        # Automatically expires unless Highlighted
            "daily_upload_limit": 100,   # Higher frequency allowed than Reels
        },
    },

    # -----------------------
    # Discord Bot / Webhook Uploads
    # -----------------------
    "discord_messaging": {
        "content_types": {"video", "image", "file"},
        "features": {
            "direct_upload": True,        # Sending file as an attachment
            "set_content": True,         # The message text (Max 2,000 characters)
            "embeds": True,              # Rich cards with titles/thumbnails
            "thread_support": True,      # Can post into specific sub-threads
            "spoiler_tag": True,         # Can mark files/text as ||spoilers||
            "webhook_support": True      # Can post without a full bot user
        },
        "limits": {
            "free_file_limit_mb": 10,     # Standard limit for free/bot accounts
            "nitro_basic_limit_mb": 50,
            "nitro_full_limit_mb": 500,
            "max_attachments_per_msg": 10,
            "character_limit": 2000,      # 4,000 for Nitro users
            "rate_limit_global": "50/sec" # Very generous compared to YouTube
        },
    },

    # -----------------------
    # Twitter Thread Posting
    # -----------------------
    "twitter_thread": {
        "api_version": "v2",
        "auth_type": "OAuth 1.0a or OAuth 2.0 PKCE",
        "features": {
            "post_text": True,           # Max 280 characters
            "reply_threading": True,     # Link tweets via in_reply_to_tweet_id
            "media_upload": True,        # Requires v1.1 endpoint (legacy but necessary)
            "link_previews": True        # Auto-generated by Twitter if link is at end
        },
        "limits": {
            "char_limit": 280,
            "daily_post_limit": 50,      # Free tier limit (approximately)
            "rate_limit": "50 per 24h"   # Strictly enforced on Free tier
        }
    },

    # -----------------------
    # Tiktok
    # -----------------------
    "tiktok_post": {
        "content_types": {"video", "photo"},
        "privacy_modes": {"PUBLIC_TO_EVERYONE", "MUTUAL_FOLLOW_FRIENDS", "FOLLOWER_OF_CREATOR", "SELF_ONLY"},
        "features": {
            "direct_post": True,         # Publish directly to profile
            "upload_to_inbox": True,     # Upload as a "Draft" notification to user
            "set_title": True,           # Max 2,200 characters (includes hashtags)
            "hashtag_support": True,     # Integrated into the title string
            "ai_labeling": True,         # REQUIRED: Must flag AI-generated content
            "commercial_disclosure": True,# REQUIRED: Flag if video is an AD/Sponsorship
            "disable_duet": True,
            "disable_stitch": True,
            "disable_comment": True,
            "video_cover_selection": True # Choose frame timestamp for thumbnail
        },
        "limits": {
            "max_duration_seconds": 600,  # 10 Minutes via API (Up to 60m for some)
            "max_file_size_mb": 500,      # Consistent across Web/API
            "aspect_ratio": "9:16",       # Strictly vertical recommended
            "daily_quota": 5,             # Limit of "pending" shares per 24h for new apps
            "rate_limit": "6 requests/min"# Per user access token
        },
    },
    # -----------------------
    # Reddit
    # -----------------------
    "reddit": {
        "role": "Moderator",
        "features": {
            "bypass_filters": True,      # If added as a Moderator
            "sticky_posts": True,        # Can pin posts to the top
            "auto_approve": True,        # Instantly approve its own content
            "flair_assignment": True,    # Set 'Mod' or 'Video' flairs
            "lock_comments": True,       # Can lock its own threads if needed
        },
        "setup_requirements": {
            "app_type": "script",        # Selected in Reddit App Preferences
            "user_agent": "platform:app_id:v1.0 (by /u/your_username)",
            "scopes": ["submit", "modposts", "identity"]
        }
    },
    # -----------------------
    # Linkedin
    # ----------------------- 
    "linkedin": {
        "author_type": "ORGANIZATION",
        "api_version": "2025-11", # LinkedIn uses versioned APIs now
        "features": {
            "direct_publish": True,      # No "Draft" mode via API for Pages
            "multi_image_support": True, # Up to 9 images per post
            "video_upload": True,        # Native video gets 5x more reach
            "document_sharing": True,    # PDF "Carousel" posts (very high engagement)
            "comment_control": True,     # Can enable/disable comments via API
            "targeting": True,           # Target by industry, seniority, or geography
            "first_comment_api": True,   # Post the first comment automatically
        },
        "limits": {
            "text_char_limit": 3000,
            "max_video_size_mb": 200,    # Strictly 200MB for Page posts (vs 5GB for Personal)
            "max_video_duration": 1800,  # 30 Minutes
            "max_image_size_mb": 5,
            "daily_post_limit": 20,      # Per-page limit for API users
            "aspect_ratio_video": ["16:9", "1:1", "4:5"], # 4:5 is best for mobile
        },
    },
    # -----------------------
    # Webtoons
    # ----------------------- 
    "webtoon_creator_post": {
        "access_method": "Headless Browser",
        "features": {
            "text_post": True,
            "image_upload": True,        # Max 10 images
            "creator_only": True,        # Must be a Canvas Creator
            "notification_push": True    # Notifies your series subscribers
        },
        "workflow": [
            "1. Login to Webtoons.com",
            "2. Navigate to Creator Profile",
            "3. Click 'Post' button via Selector",
            "4. Input content and Submit"
        ]
    },
    
    # -----------------------
    # Blues
    # ----------------------- 
    "bluesky_post": {
        "protocol": "ATProto",
        "features": {
            "text_posts": True,          # 300 character limit
            "rich_text": True,           # Facets (bold, links, mentions)
            "image_attachments": True,   # Up to 4 images
            "alt_text": True,            # Required for accessibility-focused users
            "embed_links": True,         # Card previews
            "labeling": True             # Content warnings (NSFW, etc.)
        },
        "limits": {
            "char_limit": 300,
            "max_image_mb": 1.0,         # Bluesky compresses heavily
            "daily_post_limit": 5000      # Very high/generous
        }
    },

    # -----------------------
    # Substack
    # ----------------------- 
    "substack_notes": {
        "type": "Social Feed",
        "features": {
            "post_note": True,           # Social media style posts
            "cross_post": True,          # Share your newsletter to Notes
            "image_support": True,
            "link_previews": True
        },
        "limits": {
            "auth_method": "Session Cookie", # No official API keys yet
            "note_char_limit": 1000,
            "daily_limit": "Low"         # Risk of shadowban if too fast
        }
    }
    
}