const Header = () => {
  return (
    <header className="bg-card shadow-soft px-4 py-3 flex items-center gap-3 border-b border-border">
      <div className="w-10 h-10 rounded-full bg-gradient-to-br from-pink-400 to-purple-500 flex items-center justify-center text-white font-bold text-lg">
        G
      </div>
      <div>
        <h1 className="text-xl font-bold text-foreground leading-tight">
          Sorvelinux
        </h1>
        <p className="text-xs text-muted-foreground font-medium">
          Sua sorveteria favorita bebes, agora no chat!
        </p>
      </div>
      <div className="ml-auto flex items-center gap-1">
        <span className="w-2 h-2 rounded-full bg-secondary animate-pulse" />
        <span className="text-xs text-muted-foreground">Online</span>
      </div>
    </header>
  );
};

export default Header;
