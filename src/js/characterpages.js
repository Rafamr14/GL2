const title = document.querySelector('title').textContent;

const jsonFileName = `/public/data/${title}.json`;

fetch(jsonFileName)
    .then(response => response.json())
    .then(data => {
        if (data.Name) {
            document.getElementById('character-name').textContent = data.Name;
        }
        if (data.Class) {
            document.getElementById('class-name').textContent = data.Class;
        }
        if (data.CharPortrait) {
            document.getElementById('character-portrait').src = data.CharPortrait;
        }

        const attributesBody = document.getElementById('attributes-body');
        attributesBody.innerHTML = `
            <tr><td>HP</td><td>${data.Attributes.HP}</td></tr>
            <tr><td>ATK</td><td>${data.Attributes.ATK}</td></tr>
            <tr><td>DEF</td><td>${data.Attributes.DEF}</td></tr>
            <tr><td>Stability Gauge</td><td>${data.Attributes.StabilityGauge}</td></tr>
            <tr><td>Movement Speed</td><td>${data.Attributes.MovementSpeed}</td></tr>
        `;

        // Función para generar filas de atributos
        function generateAttributeRows(skillAttribute) {
            let html = '';
            if (skillAttribute.SAtt1Image && skillAttribute.SAtt1) {
                html += `
                    <tr>
                        <td><img src="${skillAttribute.SAtt1Image}" alt="Att1"> </td>
                        <td>${skillAttribute.SAtt1}</td>
                    </tr>
                `;
            }
            if (skillAttribute.SAtt2Image && skillAttribute.SAtt2) {
                html += `
                    <tr>
                        <td><img src="${skillAttribute.SAtt2Image}" alt="Att2"> </td>
                        <td>${skillAttribute.SAtt2}</td>
                    </tr>
                `;
            }
            return html;
        }

        // Generar atributos para 'attributes-type'
        const attributesType = document.getElementById('attributes-type');
        attributesType.innerHTML = generateAttributeRows(data.SkillAttribute);

        // Generar atributos para 'attributes-typeMV'
        const attributesTypeMV = document.getElementById('attributes-typeMV');
        let attributesTypeMVHTML = generateAttributeRows(data.SkillAttribute);
        // Si necesitas añadir algo específico para 'attributesTypeMV', puedes hacerlo aquí
        attributesTypeMV.innerHTML = attributesTypeMVHTML;

        // Función para generar filas de debilidades
        function generateWeaknessRows(weakness) {
            let html = '';
            if (weakness.Weakness1Image && weakness.Weakness1) {
                html += `
                    <tr>
                        <td><img src="${weakness.Weakness1Image}" alt="Weakness1"> </td>
                        <td><b>${weakness.Weakness1}</b></td>
                    </tr>
                `;
            }
            if (weakness.Weakness2Image && weakness.Weakness2) {
                html += `
                    <tr>
                        <td><img src="${weakness.Weakness2Image}" alt="Weakness2"> </td>
                        <td><b>${weakness.Weakness2}</b></td>
                    </tr>
                `;
            }
            return html;
        }

        // Generar debilidades para 'attributes-weakness'
        const attributesWeakness = document.getElementById('attributes-weakness');
        attributesWeakness.innerHTML = generateWeaknessRows(data.Weakness);

        // Generar debilidades para 'attributes-weaknessMV'
        const attributesWeaknessMV = document.getElementById('attributes-weaknessMV');
        let attributesWeaknessMVHTML = generateWeaknessRows(data.Weakness);
        // Si necesitas añadir algo específico para 'attributesWeaknessMV', puedes hacerlo aquí
        attributesWeaknessMV.innerHTML = attributesWeaknessMVHTML;

        document.getElementById('class-image-id').src = data.ClassImage;
        document.getElementById('class-image-idMV').src = data.ClassImage;

        const effectsBody = document.getElementById('effects-body');
        if (data.Effects && data.Effects.Full) {
            const effectsSegments = data.Effects.Full.split('\n\n');
            effectsBody.innerHTML = effectsSegments.map(segment => {
                const [title, ...rest] = segment.split(':');
                const description = rest.join(':').trim();
                return `<tr><td><strong>${title}:</strong> ${description}</td></tr>`;
            }).join('');
        }

        const skillsInfo = document.getElementById('skills-info');
        const skills = [...data.Basic, ...data.Skill, ...data.Skill2, ...data.Ultimate, ...data.Passive];
        skills.forEach(skill => {
            const extraKeys = Object.keys(skill).filter(key =>
                (key.startsWith('Vertebrae') || key.startsWith('Fixed Key')) && skill[key] !== null
            );

            let extraInfoHTML = '';
            if (extraKeys.length > 0) {
                extraInfoHTML = extraKeys.map(key => `
                    <div class="mt-2">
                        <strong>${key}:</strong> ${skill[key]}
                    </div>
                `).join('');
            }

            skillsInfo.innerHTML += `
                <div class="col">
                    <div class="card">
                        <div class="card-header d-flex align-items-center">
                            <img src="${skill.SkillImage}" alt="Skill Image" class="skill-img">
                            ${skill.SkillName || ''}
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Range</th>
                                            <th>Attribute 1</th>
                                            <th>Attribute 2</th>
                                            <th>Attribute 3</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>${skill.Range || '--'}</td>
                                            <td>${skill.Att1 || '--'}</td>
                                            <td>${skill.Att2 || '--'}</td>
                                            <td>${skill.Att3 || '--'}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="row">
                                <div class="col-4">
                                    <img src="${skill.RangeImage}" alt="Range Image" class="img-fluid">
                                </div>
                                <div class="col-8 table-responsive">
                                    <p>${skill.Description}</p>
                                </div>
                            </div>
                            ${extraInfoHTML}
                        </div>
                    </div>
                </div>
            `;
        });

        const upgradesInfo = document.getElementById('upgrades-body');
        const upgradesInfoMV = document.getElementById('upgrades-bodyMV');

        Object.keys(data.Upgrades).forEach(level => {
            data.Upgrades[level].forEach(upgrade => {
                upgradesInfo.innerHTML += `
                    <tr>
                        <td class="bg-dark text-center">
                            <img src="${upgrade.IconImage}" alt="Icon" class="upgrade-icon">
                        </td>
                        <td>${level}</td>
                        <td><b>${upgrade.SkillName}</b></td>
                        <td>${upgrade.Effect.replace(/\n/g, '<br>')}</td>
                    </tr>
                `;

                upgradesInfoMV.innerHTML += `
                    <tr>
                        <td class="bg-dark text-center">
                            <img src="${upgrade.IconImage}" alt="Icon" class="upgrade-icon">
                        </td>
                        <td>${level}</td>
                        <td><b>${upgrade.SkillName}</b></td>
                    </tr>
                    <tr>
                        <td colspan="3" class="effect-header">
                            Effect
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3">
                            ${upgrade.Effect.replace(/\n/g, '<br>')}
                        </td>
                    </tr>
                `;
            });
        });
    })
    .catch(error => console.error('Error fetching JSON:', error));

function changeImage(imageUrl) {
    document.getElementById('character-portrait').src = imageUrl;
    document.getElementById('character-imageMV').src = imageUrl;
}

document.querySelectorAll('.btn-custom').forEach(button => {
    button.addEventListener('click', function() {
        const imageUrl = this.getAttribute('data-image');
        changeImage(imageUrl);
    });
});
