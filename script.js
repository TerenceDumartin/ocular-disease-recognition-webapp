const odrApiUrl = 'https://odrdockerimage-4rkl6m35oq-ew.a.run.app/predict/';

const predict = () => {
  form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = {
        "X": document.getElementById('imageDrop'),
      };
      let query = []
      Object.keys(data).forEach((param) => {
        query.push(`${param}=${data[param]}`)
      })
      const querystring = query.join('&')
      const url = `${odrApiUrl}?${querystring}`
      fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('fare').classList.remove('d-none');
        const fareResult = document.getElementById('predicted-fare');
        const fare = (data["X"])
        fareResult.innerText = `${fare}`;
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });
  }
};


predict();
