def split_title_into_parts(title, max_length=55):
    parts = []
    while len(title) > max_length:
        # Find the last space within the max_length limit
        split_index = title.rfind(' ', 0, max_length)
        
        if split_index == -1:  # No space found, force split at max_length
            split_index = max_length

        # Append the current part and update the title
        parts.append(title[:split_index].strip())
        title = title[split_index:].strip()

    # Add the remaining part
    if title:
        parts.append(title)

    return parts

# Example usage
title = "An example of a long title that needs to be divided into multiple parts where each can have up to 55 characters."
parts = split_title_into_parts(title)
print(parts)
print(split_title_into_parts("যুক্তরাজ্যের নতুন অভিবাসন নীতি ঘোষণা, চা ও বিস্কুট আনলে লাগবে না ভিসা"))