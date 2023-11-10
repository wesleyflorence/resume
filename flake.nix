{
  description = "Resume project for local development";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system: 
      let
        pkgs = nixpkgs.legacyPackages.${system};
        zsh = pkgs.zsh;
        tex = pkgs.texlive.combined.scheme-full;
        entr = pkgs.entr;
        zathura = pkgs.zathura;
        pandoc = pkgs.pandoc;
      in

      {
        devShell = pkgs.mkShell {
          buildInputs = [ zsh tex entr zathura pandoc ];
          SHELL = "${pkgs.zsh}/bin/zsh";
          shellHook = ''
            if [ -z "$IN_NIX_SHELL_ZSH_STARTED" ]; then
              export IN_NIX_SHELL_ZSH_STARTED=1
              exec $SHELL
            fi
          '';
        };
      }
    );
}


