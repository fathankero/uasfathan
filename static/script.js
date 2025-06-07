function startRecognition() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'id-ID';
  recognition.start();

  recognition.onresult = function(event) {
    const text = event.results[0][0].transcript;
    document.getElementById('original').innerText = text;

    fetch('/translate', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({text: text})
    })
    .then(res => res.json())
    .then(data => {
      const translatedText = data.translated;
      document.getElementById('translated').innerText = translatedText;

      // Tambahkan bagian ini untuk text-to-speech:
      const utterance = new SpeechSynthesisUtterance(translatedText);
      utterance.lang = 'ja-JP'; // bahasa Jepang untuk suara
      window.speechSynthesis.speak(utterance);
    });
  };
}
