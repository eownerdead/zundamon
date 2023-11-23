{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    utils.url = "github:numtide/flake-utils";
    psd2svg = {
      url = "github:eownerdead/psd2svg";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, utils, psd2svg }:
    utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in rec {
        formatter = pkgs.nixfmt;

        devShells.default = pkgs.mkShell {
          packages = (with pkgs; [ editorconfig-checker nixfmt statix ]) ++ ([
            psd2svg.packages."${system}".psd2svg
          ]);
        };
      });
}
