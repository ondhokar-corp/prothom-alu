module Jekyll
  module BanglaNumbers
    def bangla_number(input)
      bangla_digits = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]
      input.to_s.chars.map { |char| bangla_digits[char.to_i] }.join
    end
  end
end

Liquid::Template.register_filter(Jekyll::BanglaNumbers)
