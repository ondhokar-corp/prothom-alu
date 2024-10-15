require 'uglifier'


Jekyll::Hooks.register :site, :post_write do |site|
js_files = Dir.glob(File.join(site.dest, '**', '*.js'))

js_files.each do |file|
# Enable harmony mode for ES6+ syntax support
minified_js = Uglifier.new(
  harmony: true,
  mangle: true,
  compress: {
    unused: true, # Drop unreferenced functions and variables
   dead_code: true, # Remove unreachable code
    drop_console: true # Remove console.* calls
  }
).compile(File.read(file))
File.write(file, minified_js)
end
end