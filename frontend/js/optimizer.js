const form = document.getElementById("optimizerForm");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const crop = document.getElementById("crop").value;
    const soil = document.getElementById("soil").value;

    const nitrogen = Number(
        document.getElementById("nitrogen").value
    );

    const phosphorus = Number(
        document.getElementById("phosphorus").value
    );

    const potassium = Number(
        document.getElementById("potassium").value
    );

    const ph = Number(
        document.getElementById("ph").value
    );

    const temperature = Number(
        document.getElementById("temperature").value
    );

    const rainfall = Number(
        document.getElementById("rainfall").value
    );

    const area = Number(
        document.getElementById("area").value
    );


    // Temporary recommendation logic
    // We will replace this with our real model later.

    const recommendedN = Math.max(nitrogen * 0.90, 0);
    const recommendedP = Math.max(phosphorus * 0.90, 0);
    const recommendedK = Math.max(potassium * 0.90, 0);

    const fertilizerReduction =
        ((nitrogen + phosphorus + potassium) -
        (recommendedN + recommendedP + recommendedK))
        /
        (nitrogen + phosphorus + potassium) * 100;


    const expectedYield =
        3 +
        (ph * 0.1) +
        (rainfall / 2000) +
        (temperature / 100);


    const result = document.querySelector(".result-container");


    result.innerHTML = `

        <h2>🌱 Fertilizer Recommendation</h2>

        <p><strong>Crop:</strong> ${crop}</p>

        <p><strong>Soil Type:</strong> ${soil}</p>

        <div class="recommendation-grid">

            <div>
                <h3>Nitrogen</h3>
                <p>${recommendedN.toFixed(1)} kg/ha</p>
            </div>

            <div>
                <h3>Phosphorus</h3>
                <p>${recommendedP.toFixed(1)} kg/ha</p>
            </div>

            <div>
                <h3>Potassium</h3>
                <p>${recommendedK.toFixed(1)} kg/ha</p>
            </div>

        </div>

        <p>
            <strong>Estimated Yield:</strong>
            ${expectedYield.toFixed(2)} tonnes/ha
        </p>

        <p>
            <strong>Fertilizer Reduction:</strong>
            ${fertilizerReduction.toFixed(1)}%
        </p>

        <p>
            <strong>Land Area:</strong>
            ${area} hectares
        </p>

    `;

});