let cards = [];
let current = 0;

fetch('flashcards.json')
  .then(res => res.json())
  .then(data => {
      cards = data;
      showCard();
  });

const cardElem = document.getElementById('card');
const wordElem = document.getElementById('word');
const phoneticElem = document.getElementById('phonetic');
const sentenceElem = document.getElementById('sentence');
const chineseElem = document.getElementById('chinese');
const nextBtn = document.getElementById('next');

cardElem.addEventListener('click', () => {
    cardElem.classList.toggle('flipped');
});

nextBtn.addEventListener('click', () => {
    current = (current + 1) % cards.length;
    cardElem.classList.remove('flipped');
    showCard();
});

function showCard() {
    const item = cards[current];
    wordElem.textContent = item.word;
    phoneticElem.textContent = item.phonetic;
    sentenceElem.textContent = item.example;
    chineseElem.textContent = item.chinese;
}
