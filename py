onValue(ledRef, (snapshot) => {

    if (snapshot.exists()) {

      const led = snapshot.val();

      Object.keys(led).forEach((key, index) => {

        const checkbox = document.getElementById(`checkbox-${index + 1}`);

        if (checkbox) { 

          checkbox.checked = led[key] === 1;

        }

      });

      console.log("Status LED berubah:", led);

    } else {

      console.log("Data LED tidak ditemukan");

    }

  });



  // Mendengarkan perubahan sensor DHT

  onValue(

    dhtRef,

    (snapshot) => {

      if (snapshot.exists()) {

        const data = snapshot.val();

        let temperature  = data.temperature;

        let humid = data.humid;

        console.log("Temperature update:", temperature);

        console.log("Humidity update:", humid);

        updateWeather(temperature, humid);

      } else {

        console.log("Data DHT tidak ditemukan");

      }

    },

    (error) => {

      console.log("Error membaca data DHT:", error);

    }

  );



  // Mendengarkan perubahan sensor Ultrasonic

  onValue(usRef, (snapshot) => {

    if (snapshot.exists()) {

      const data = snapshot.val();

      console.log("Jarak berubah:", data.jarak);



      const barPercentElement = document.querySelector(".bar_percent");

      if (barPercentElement) {

        barPercentElement.style.setProperty("--num", data.jarak);

      }



      const percentageElement = document.getElementById("nilaisuhu");

      if (percentageElement) {

        percentageElement.textContent = `${data.jarak} Cm`;

      }

    } else {

      console.log("Data Ultrasonic tidak ditemukan");

    }

  });



  // Fungsi untuk mengontrol LED dari checkbox

  window.toggleLED = () => {

    const ledState = [1, 2, 3].map((i) =>

      document.getElementById(`checkbox-${i}`).checked ? 1 : 0

    );



    set(ledRef, {

      led1: ledState[0],

      led2: ledState[1],

      led3: ledState[2],

    })

      .then(() => console.log("LED state updated in Firebase"))

      .catch(() => console.log("Gagal memperbarui status LED"));

  };

</script>onValue(ledRef, (snapshot) => {

    if (snapshot.exists()) {

      const led = snapshot.val();

      Object.keys(led).forEach((key, index) => {

        const checkbox = document.getElementById(`checkbox-${index + 1}`);

        if (checkbox) { 

          checkbox.checked = led[key] === 1;

        }

      });

      console.log("Status LED berubah:", led);

    } else {

      console.log("Data LED tidak ditemukan");

    }

  });



  // Mendengarkan perubahan sensor DHT

  onValue(

    dhtRef,

    (snapshot) => {

      if (snapshot.exists()) {

        const data = snapshot.val();

        let temperature  = data.temperature;

        let humid = data.humid;

        console.log("Temperature update:", temperature);

        console.log("Humidity update:", humid);

        updateWeather(temperature, humid);

      } else {

        console.log("Data DHT tidak ditemukan");

      }

    },

    (error) => {

      console.log("Error membaca data DHT:", error);

    }

  );



  // Mendengarkan perubahan sensor Ultrasonic

  onValue(usRef, (snapshot) => {

    if (snapshot.exists()) {

      const data = snapshot.val();

      console.log("Jarak berubah:", data.jarak);



      const barPercentElement = document.querySelector(".bar_percent");

      if (barPercentElement) {

        barPercentElement.style.setProperty("--num", data.jarak);

      }



      const percentageElement = document.getElementById("nilaisuhu");

      if (percentageElement) {

        percentageElement.textContent = `${data.jarak} Cm`;

      }

    } else {

      console.log("Data Ultrasonic tidak ditemukan");

    }

  });



  // Fungsi untuk mengontrol LED dari checkbox

  window.toggleLED = () => {

    const ledState = [1, 2, 3].map((i) =>

      document.getElementById(`checkbox-${i}`).checked ? 1 : 0

    );



    set(ledRef, {

      led1: ledState[0],

      led2: ledState[1],

      led3: ledState[2],

    })

      .then(() => console.log("LED state updated in Firebase"))

      .catch(() => console.log("Gagal memperbarui status LED"));

  };

</script>
