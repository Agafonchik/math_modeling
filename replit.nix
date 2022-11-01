{ pkgs }: {
    deps = [
        pkgs.python39Packages.pip
        pkgs.ihaskell
        pkgs.cowsay
    ];
}