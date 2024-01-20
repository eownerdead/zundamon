{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    utils.url = "github:numtide/flake-utils";
    psd2svg = {
      url = "github:eownerdead/psd2svg";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    mame.url = "git+https://codeberg.org/eownerdead/mame";
  };

  outputs = { self, nixpkgs, utils, psd2svg, mame }:
    utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in rec {
        formatter = pkgs.nixfmt;

        packages.readmePage = mame.lib."${system}".renderPage {
          src = ./README.md;
        };

        devShells.default = pkgs.mkShell {
          packages = (with pkgs; [
            editorconfig-checker
            nixfmt
            statix
            python3
            ruff
            markdownlint-cli2
          ]) ++ [ psd2svg.packages."${system}".psd2svg ];
        };
      });
}
