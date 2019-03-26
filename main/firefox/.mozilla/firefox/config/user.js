// Minhas alterações ao about:config do Firefox
//
// Rafael Cavalcanti


// Arch Wiki
user_pref("security.ssl3.dhe_rsa_aes_256_sha", false);
user_pref("security.ssl3.dhe_rsa_aes_128_sha", false);
user_pref("geo.enabled", false);
// This option breaks 360 videos
//user_pref("webgl.disabled", true);


// ==================================================================
// Annoyances, workflow
// ==================================================================

// Não verificar se é navegador padrão
user_pref("browser.shell.checkDefaultBrowser", false);

// Não mostrar "one-click search engines" na barra de endereços
user_pref("browser.urlbar.oneOffSearches", false);

// Não tocar vídeo até estar em primeiro plano
// (padrão em 56+)
user_pref("media.block-autoplay-until-in-foreground", true);

// Não mostrar aviso de tela cheia
user_pref("full-screen-api.warning.timeout", 0);

// Não auto-esconder barras de ferramentas em modo de tela cheia
user_pref("browser.fullscreen.autohide", false);

// Abrir nova janela em nova aba
user_pref("browser.link.open_newwindow.restriction", 0);

// Abrir "Buscar no Google" do menu de contexto em segundo plano
user_pref("browser.search.context.loadInBackground", true);


// ==================================================================
// Daqui pra baixo, o que mexi pela GUI e achei no pref.js
// ==================================================================

// Restaurar sessão ao iniciar
user_pref("browser.startup.page", 3);

// Não aceitar third-party cookies
user_pref("network.cookie.cookieBehavior", 1);

// Trocar fontes para as usadas no Chrome (na GUI em "Advanced")
user_pref("font.name.monospace.x-western", "monospace");
user_pref("font.name.sans-serif.x-western", "Arial");
user_pref("font.name.serif.x-western", "Times New Roman");

// Habilitar autorolagem
user_pref("general.autoScroll", true);

//// Adicionar Blogtrotrr como feed reader (aparente resultado de ter clicado no link
//// para tal no site deles)
//user_pref("browser.contentHandlers.types.6.title", "Blogtrottr");
//user_pref("browser.contentHandlers.types.6.type", "application/vnd.mozilla.maybe.feed");
//user_pref("browser.contentHandlers.types.6.uri", "https://blogtrottr.com/?subscribe=%s");