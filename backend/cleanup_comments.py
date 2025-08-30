#!/usr/bin/env python3
"""
Cleanup script to remove all comment-related data from the database.
This script removes:
1. All documents from the post_comments collection
2. The comments_count field from all community_posts documents
"""

import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def cleanup_comments():
    """Remove all comment-related data from the database"""
    
    # Get MongoDB connection
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mood_journal_db')
    
    try:
        client = MongoClient(mongo_uri)
        db = client.get_default_database()
        
        print("Connected to MongoDB successfully")
        
        # 1. Remove all documents from post_comments collection
        if 'post_comments' in db.list_collection_names():
            result = db.post_comments.delete_many({})
            print(f"Deleted {result.deleted_count} comments from post_comments collection")
        else:
            print("post_comments collection does not exist")
        
        # 2. Remove comments_count field from all community_posts documents
        if 'community_posts' in db.list_collection_names():
            result = db.community_posts.update_many(
                {}, 
                {'$unset': {'comments_count': ''}}
            )
            print(f"Removed comments_count field from {result.modified_count} community posts")
        else:
            print("community_posts collection does not exist")
        
        # 3. Drop the post_comments collection entirely
        if 'post_comments' in db.list_collection_names():
            db.post_comments.drop()
            print("Dropped post_comments collection")
        
        print("Comment cleanup completed successfully!")
        
    except Exception as e:
        print(f"Error during cleanup: {e}")
        sys.exit(1)
    finally:
        client.close()

if __name__ == '__main__':
    print("Starting comment cleanup...")
    cleanup_comments()
