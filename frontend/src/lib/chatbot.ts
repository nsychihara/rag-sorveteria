interface BotResponse {
  text: string;
  suggestions?: string[];
}

const responses: { keywords: string[]; response: BotResponse }[] = [
  {
    keywords: ["sabor", "sabores", "cardápio", "opções", "opção"],
    response: {
      text: "🍨 Nossos sabores mais pedidos:\n\n• Morango com Leite Ninho\n• Chocolate Belga\n• Açaí com Granola\n• Pistache Italiano\n• Maracujá Cremoso\n• Manga com Pimenta\n\nQuer saber mais sobre algum?",
      suggestions: ["Preços", "Promoções", "Tamanhos"],
    },
  },
  {
    keywords: ["preço", "preços", "valor", "quanto custa", "custa"],
    response: {
      text: "💰 Nossos preços:\n\n• Casquinha simples: R$ 8,00\n• Casquinha dupla: R$ 12,00\n• Copão 300ml: R$ 15,00\n• Copão 500ml: R$ 22,00\n• Milk-shake: R$ 18,00\n• Açaí 300ml: R$ 16,00",
      suggestions: ["Sabores", "Promoções", "Horário"],
    },
  },
  {
    keywords: ["horário", "horarios", "horario", "funciona", "abre", "fecha", "aberto"],
    response: {
      text: "🕐 Nosso horário de funcionamento:\n\n• Segunda a Sexta: 10h às 22h\n• Sábado: 10h às 23h\n• Domingo: 12h às 21h\n\nEstamos sempre prontos pra te receber! 😊",
      suggestions: ["Localização", "Sabores", "Promoções"],
    },
  },
  {
    keywords: ["promoção", "promoções", "desconto", "oferta"],
    response: {
      text: "🎉 Promoções da semana:\n\n🔥 Terça Dupla: Pague 1, leve 2 casquinhas!\n🔥 Quinta do Açaí: Açaí 500ml por R$ 19,90\n🔥 Combo Família (sábado): 4 copões por R$ 49,90\n\nAproveite! 🍦",
      suggestions: ["Sabores", "Preços", "Horário"],
    },
  },
  {
    keywords: ["localização", "endereço", "onde", "local", "como chegar"],
    response: {
      text: "📍 Estamos na Rua das Flores, 123 — Centro.\n\nPonto de referência: ao lado da praça principal.\n\nTambém fazemos delivery pelo app! 🛵",
      suggestions: ["Horário", "Sabores", "Delivery"],
    },
  },
  {
    keywords: ["delivery", "entrega", "entregar"],
    response: {
      text: "🛵 Sim! Fazemos delivery!\n\nPedido mínimo: R$ 20,00\nTaxa de entrega: R$ 5,00 (grátis acima de R$ 50)\nTempo médio: 30 a 45 minutos\n\nPeça pelo nosso chat ou pelo app!",
      suggestions: ["Sabores", "Preços", "Promoções"],
    },
  },
  {
    keywords: ["tamanho", "tamanhos", "porção", "porções"],
    response: {
      text: "📏 Tamanhos disponíveis:\n\n• Mini (150ml) — perfeito pra provar\n• Médio (300ml) — nosso queridinho\n• Grande (500ml) — pra quem ama sorvete\n• Mega (750ml) — pra compartilhar! 🤩",
      suggestions: ["Preços", "Sabores"],
    },
  },
  {
    keywords: ["oi", "olá", "ola", "hey", "bom dia", "boa tarde", "boa noite", "eae", "e aí"],
    response: {
      text: "Olá! 🍦 Bem-vindo(a) à Gelato Chat!\n\nSou seu assistente virtual. Como posso te ajudar hoje?",
      suggestions: ["Sabores", "Preços", "Promoções", "Horário"],
    },
  },
  {
    keywords: ["obrigado", "obrigada", "valeu", "agradeço", "thanks"],
    response: {
      text: "De nada! 😊 Foi um prazer ajudar! Se precisar de mais alguma coisa, estou por aqui. Bom sorvete! 🍨",
      suggestions: ["Sabores", "Promoções"],
    },
  },
];

const fallback: BotResponse = {
  text: "Hmm, não entendi muito bem 🤔\nPosso te ajudar com informações sobre sabores, preços, promoções, horários e muito mais!",
  suggestions: ["Sabores", "Preços", "Promoções", "Horário"],
};

export function getBotResponse(userMessage: string): BotResponse {
  const lower = userMessage.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  for (const entry of responses) {
    if (entry.keywords.some((kw) => lower.includes(kw.normalize("NFD").replace(/[\u0300-\u036f]/g, "")))) {
      return entry.response;
    }
  }

  return fallback;
}
