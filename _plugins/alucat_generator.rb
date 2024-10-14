# _plugins/alucats_generator.rb

module Jekyll
  class AlucatsGenerator < Generator
    safe true
    priority :low

    def generate(site)
      # Initialize alucats data as an array
      site.data['alucats'] = []

      # Create a hash to track main categories and their subcategories
      categories_hash = {}

      # Iterate through all the posts in the site
      site.posts.docs.each do |post|
        # Split the post's path and find the main category
        path_parts = post.path.split(File::SEPARATOR)
        main_category_index = path_parts.index("p") + 2 # Assumes /p/News/National/_posts/post.md
        main_category = path_parts[main_category_index] || "Uncategorized"

        # Initialize the subcategories array for the main category if not already done
        categories_hash[main_category] ||= []

        # Add subcategories from post's front matter 'categories', filtering out "p" and "News"
        if post.data['categories']
          post.data['categories'].each do |subcategory|
            unless ["p", "News"].include?(subcategory) || subcategory == main_category || categories_hash[main_category].include?(subcategory)
              categories_hash[main_category] << subcategory
            end
          end
        end
      end

      # Convert categories_hash to the desired array format for alucats
      categories_hash.each do |main_category, subcategories|
        site.data['alucats'] << {
          'title' => main_category,
          'subcategories' => subcategories
        }
      end
    end
  end
end
