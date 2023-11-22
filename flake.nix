{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in rec {
        packages.psd2svg = pkgs.python3.pkgs.buildPythonPackage rec {
          pname = "psd2svg";
          version = "0.2.3";
          format = "setuptools";

          doCheck = false;

          src = pkgs.fetchPypi {
            inherit pname version;
            hash = "sha256-GuzNCFXCDM95f62+14Kk7OiTfX91EJdPz4ggziO/OPQ=";
          };

          propagatedBuildInputs = with pkgs.python3Packages; [
            psd-tools
            svgwrite
            future
          ];

          postPatch = ''
            substituteInPlace setup.py --replace \'pytest-runner\' ""
          '';
        };

        formatter = pkgs.nixfmt;

        devShells.default = pkgs.mkShell {
          packages = (with pkgs; [ editorconfig-checker nixfmt statix ]) ++ ([
            packages.psd2svg
          ]);
        };
      });
}
