class Eject < Formula
  desc "Force ejecting external drive on macOS"
  homepage "https://github.com/honzajavorek/eject"
  url "https://github.com/honzajavorek/eject/archive/v1.0.0.zip"
  version "1.0.0"
  sha256 "39849bbb249bfd94491fffa4c140c4ae0e26f4b66565a9f0e506e879cfc08359"

  depends_on "python" => "3"

  def install
    bin.install "eject"
  end

  test do
    system "which eject"
  end
end
