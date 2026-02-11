interface QuickRepliesProps {
  suggestions: string[];
  onSelect: (text: string) => void;
}

const QuickReplies = ({ suggestions, onSelect }: QuickRepliesProps) => {
  if (suggestions.length === 0) return null;

  return (
    <div className="flex flex-wrap gap-2 px-4 py-2 animate-fade-in-up">
      {suggestions.map((s) => (
        <button
          key={s}
          onClick={() => onSelect(s)}
          className="text-xs font-semibold px-3 py-1.5 rounded-full bg-primary/10 text-primary border border-primary/20 hover:bg-primary/20 transition-colors duration-200"
        >
          {s}
        </button>
      ))}
    </div>
  );
};

export default QuickReplies;
