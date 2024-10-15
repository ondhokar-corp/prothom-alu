require 'htmlcompressor'

Jekyll::Hooks.register :site, :post_render do |site|
  compressor = HtmlCompressor::Compressor.new

  site.pages.each do |page|
    next unless page.output_ext == '.html'

    # Minify the HTML content
    page.output = compressor.compress(page.output)
  end
end
