import Header from "@/components/chat/Header";
import Footer from "@/components/chat/Footer";
import ChatContainer from "@/components/chat/ChatContainer";

const Index = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-muted/50 p-2 sm:p-4">
      <div className="w-full max-w-3xl h-[95vh] sm:h-[85vh] flex flex-col bg-card rounded-2xl shadow-card overflow-hidden border border-border">
        <Header />
        <ChatContainer />
        <Footer />
      </div>
    </div>
  );
};

export default Index;
