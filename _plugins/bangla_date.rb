# _plugins/bangla_date.rb
module Jekyll
  module BanglaDateFilter
    # Bangla date formatting method
    def bangla_date(input)
      # Convert the input date to the desired format
      date = Date.parse(input.to_s)

      # Define Bangla numerals and month names
      bangla_numerals = %w[০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯]
      bangla_months = [
        "জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন",
        "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"
      ]

      # Format the date components
      day = date.day.to_s.chars.map { |c| bangla_numerals[c.to_i] }.join
      month = bangla_months[date.month - 1]
      year = date.year.to_s.chars.map { |c| bangla_numerals[c.to_i] }.join

      # Return the formatted Bangla date
      "#{month} #{day}, #{year}"
    end
  end
end

Liquid::Template.register_filter(Jekyll::BanglaDateFilter)
