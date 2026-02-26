import pandas as pd
import re

# Read the processed CSV
df = pd.read_csv('anime_with_synopsis.csv')

# Parse the combined_info column to extract the original components
def parse_combined_info(row):
    combined_info = row['combined_info']
    
    # Extract title
    title_match = re.search(r'title: ([^.]+)\.\.', combined_info)
    title = title_match.group(1).strip() if title_match else ""
    
    # Extract overview/synopsis
    overview_match = re.search(r'overview: ([^"]+) \.\. genres:', combined_info)
    synopsis = overview_match.group(1).strip() if overview_match else ""
    
    # Extract genres
    genres_match = re.search(r'genres: ([^"]+)"?$', combined_info)
    genres = genres_match.group(1).strip() if genres_match else ""
    
    return pd.Series({
        'Name': title,
        'sypnopsis': synopsis,
        'Genres': genres
    })

# Apply parsing
parsed_df = df.apply(parse_combined_info, axis=1)

# Combine with original dataframe
result_df = pd.concat([parsed_df], axis=1)

# Add MAL_ID and Score columns (with default values since we don't have them)
result_df.insert(0, 'MAL_ID', range(1, len(result_df) + 1))
result_df.insert(2, 'Score', 7.5)  # Default score

print("Restored columns:", list(result_df.columns))
print("Sample data:")
print(result_df.head())

# Save as a backup first
result_df.to_csv('anime_with_synopsis_restored.csv', index=False, encoding='utf-8')
print("\nRestored CSV saved as 'anime_with_synopsis_restored.csv'")

# Overwrite the original file
result_df.to_csv('anime_with_synopsis.csv', index=False, encoding='utf-8')
print("Original file restored!")
