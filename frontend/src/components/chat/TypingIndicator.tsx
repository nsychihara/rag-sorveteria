import { IceCream } from "lucide-react";

const TypingIndicator = () => {
  return (
    <div className="flex items-end gap-2 justify-start animate-fade-in-up">
      <div className="w-8 h-8 rounded-full bg-secondary flex items-center justify-center flex-shrink-0 shadow-soft">
        <IceCream className="w-4 h-4 text-secondary-foreground" />
      </div>
      <div className="chat-bubble-bot px-4 py-3 shadow-soft flex items-center gap-1">
        <span className="w-2 h-2 rounded-full bg-chat-bot-foreground/60 animate-typing-dot-1" />
        <span className="w-2 h-2 rounded-full bg-chat-bot-foreground/60 animate-typing-dot-2" />
        <span className="w-2 h-2 rounded-full bg-chat-bot-foreground/60 animate-typing-dot-3" />
      </div>
    </div>
  );
};

export default TypingIndicator;
