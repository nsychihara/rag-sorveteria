import { IceCream, MapPin, Clock } from "lucide-react";

const Footer = () => {
  return (
    <footer className="bg-card border-t border-border px-4 py-3">
      <div className="flex flex-wrap items-center justify-center gap-4 text-xs text-muted-foreground">
        <span className="flex items-center gap-1">
          <IceCream className="w-3.5 h-3.5 text-primary" />
          Sorvelinux Chat
        </span>
        <span className="flex items-center gap-1">
          <MapPin className="w-3.5 h-3.5 text-primary" />
          Rua Nove de Julho, 859
        </span>
        <span className="flex items-center gap-1">
          <Clock className="w-3.5 h-3.5 text-primary" />
          8h às 18h
        </span>
      </div>
    </footer>
  );
};

export default Footer;
