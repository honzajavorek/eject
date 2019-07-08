class Eject < Formula
  desc "Force ejecting external drive on macOS"
  homepage "https://github.com/honzajavorek/eject"
  url "https://github.com/honzajavorek/eject/archive/v1.0.1.zip"
  version "1.0.1"
  sha256 "f69dec5fffd3d59a55152132199c32a1df177f574fc59b62ee737c6febf845e8"

  depends_on "python" => "3"

  def install
    bin.install "eject"
  end

  test do
    system "which eject"
  end
end
