-- ================================================
-- Script SQL: Sistema de Cache FAQ
-- ================================================

-- Criar tabela de cache de respostas
CREATE TABLE IF NOT EXISTS cache_respostas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pergunta_hash VARCHAR(32) NOT NULL,
    pergunta_original TEXT NOT NULL,
    resposta TEXT NOT NULL,
    hits INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_hit TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    
    -- Índices para performance
    UNIQUE KEY idx_hash (pergunta_hash),
    INDEX idx_ativo (ativo),
    INDEX idx_hits (hits DESC),
    INDEX idx_last_hit (last_hit)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ================================================
-- Popular com FAQs comuns (exemplos)
-- ================================================

INSERT INTO cache_respostas (pergunta_hash, pergunta_original, resposta, hits, ativo) VALUES
(MD5('quais os planos'), 
 'Quais os planos?',
 'Temos 3 planos disponíveis:\n\nEssencial: R$ 49,90 - Assistência funeral básica e suporte familiar.\n\nFamiliar Plus: R$ 79,90 - Inclui cliniprev, clube de vantagens e assistência ortopédica.\n\nPremium: R$ 109,90 - Cobertura completa com atendimento prioritário.\n\nQual plano te interessa?',
 0,
 TRUE),

(MD5('qual o preço'), 
 'Qual o preço?',
 'Nossos planos variam de R$ 49,90 a R$ 109,90 mensais.\n\nEssencial: R$ 49,90\nFamiliar Plus: R$ 79,90\nPremium: R$ 109,90\n\nQual plano gostaria de conhecer melhor?',
 0,
 TRUE),

(MD5('como contratar'), 
 'Como contratar?',
 'Para contratar é muito simples:\n\n1. Escolha o plano ideal\n2. Entre em contato conosco pelo WhatsApp ou telefone\n3. Nossa equipe fará o cadastro\n4. Pronto! Você já estará protegido.\n\nPosso te ajudar com mais alguma informação?',
 0,
 TRUE),

(MD5('qual a carência'), 
 'Qual a carência?',
 'Todos os planos possuem carência de 30 dias para utilização dos serviços.\n\nApós esse período, você já pode usufruir de todos os benefícios do seu plano.\n\nTem mais alguma dúvida?',
 0,
 TRUE),

(MD5('plano premium'), 
 'Me fale do plano premium',
 'O Plano Premium é nosso plano mais completo!\n\nBenefícios:\n- Cobertura completa de serviços\n- Atendimento prioritário 24h\n- Rede ampliada de atendimento\n- Todos os serviços inclusos\n\nValor: R$ 109,90 por mês\n\nGostaria de contratar?',
 0,
 TRUE);

-- ================================================
-- View para análise de FAQs
-- ================================================

CREATE OR REPLACE VIEW v_top_faqs AS
SELECT 
    id,
    pergunta_original,
    hits,
    DATE(created_at) as data_criacao,
    DATE(last_hit) as ultimo_acesso,
    DATEDIFF(NOW(), last_hit) as dias_sem_uso
FROM cache_respostas
WHERE ativo = TRUE
ORDER BY hits DESC
LIMIT 20;

-- ================================================
-- Procedure para limpar cache antigo
-- ================================================

DELIMITER //

CREATE PROCEDURE sp_limpar_cache_antigo(IN dias_inativo INT)
BEGIN
    UPDATE cache_respostas
    SET ativo = FALSE
    WHERE last_hit < DATE_SUB(NOW(), INTERVAL dias_inativo DAY)
    AND ativo = TRUE;
    
    SELECT ROW_COUNT() as registros_desativados;
END //

DELIMITER ;

-- ================================================
-- Event para limpeza automática mensal
-- ================================================

-- Ativar event scheduler
SET GLOBAL event_scheduler = ON;

-- Criar event de limpeza (roda todo dia 1 às 3h)
CREATE EVENT IF NOT EXISTS evt_limpar_cache_mensal
ON SCHEDULE EVERY 1 MONTH
STARTS (TIMESTAMP(CURRENT_DATE) + INTERVAL 1 MONTH + INTERVAL 3 HOUR)
DO
    CALL sp_limpar_cache_antigo(90);

-- ================================================
-- Consultas úteis
-- ================================================

-- Ver top 10 perguntas mais frequentes
-- SELECT * FROM v_top_faqs LIMIT 10;

-- Ver estatísticas gerais
-- SELECT 
--     COUNT(*) as total_perguntas,
--     SUM(hits) as total_hits,
--     AVG(hits) as media_hits,
--     MAX(hits) as max_hits
-- FROM cache_respostas
-- WHERE ativo = TRUE;

-- Buscar por palavra-chave
-- SELECT pergunta_original, hits, last_hit
-- FROM cache_respostas
-- WHERE pergunta_original LIKE '%plano%'
-- AND ativo = TRUE
-- ORDER BY hits DESC;