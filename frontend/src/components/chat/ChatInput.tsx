import { useState } from "react";
import { Send } from "lucide-react";

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

const ChatInput = ({ onSend, disabled }: ChatInputProps) => {
  const [text, setText] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-card border-t border-border px-4 py-3"
    >
      <div className="flex items-center gap-2 bg-muted rounded-full px-4 py-1.5 shadow-soft transition-shadow focus-within:ring-2 focus-within:ring-ring/30">
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Digite sua mensagem..."
          disabled={disabled}
          className="flex-1 bg-transparent text-sm text-foreground placeholder:text-muted-foreground outline-none py-1.5 font-body"
        />
        <button
          type="submit"
          disabled={!text.trim() || disabled}
          className="w-9 h-9 rounded-full bg-primary text-primary-foreground flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95 disabled:opacity-40 disabled:hover:scale-100"
        >
          <Send className="w-4 h-4" />
        </button>
      </div>
    </form>
  );
};

export default ChatInput;
