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
        const attributesType = document.getElementById('attributes-type');
        attributesType.innerHTML = `
                <tr>
                <td><img src="${data.SkillAttribute.SAtt1Image}" alt="Att1"> </td>
                <td>${data.SkillAttribute.SAtt1}</td>
                </tr>
                <tr>
                <td><img src="${data.SkillAttribute.SAtt2Image}" alt="Att2"> </td>
                <td>${data.SkillAttribute.SAtt2}</td>
                </tr>
            `;
        const attributesTypeMV = document.getElementById('attributes-typeMV');
        attributesTypeMV.innerHTML = `
                <tr>
                <td><img src="${data.SkillAttribute.SAtt1Image}" alt="Att1"> </td>
                <td>${data.SkillAttribute.SAtt1}</td>
                </tr>
                <tr>
                <td><img src="${data.SkillAttribute.SAtt2Image}" alt="Att2"> </td>
                <td><b></b>${data.SkillAttribute.SAtt2}</td>
                </tr>
            `;
        const attributesweakness = document.getElementById('attributes-weakness');
        attributesweakness.innerHTML = `
                <tr>
                <td><img src="${data.Weakness.Weakness1Image}" alt="Weakness1"> </td>
                <td><b> ${data.Weakness.Weakness1}</b></td></tr>
                <tr>
                <td><img src="${data.Weakness.Weakness2Image}" alt="Weakness2"> </td>
                <td><b> ${data.Weakness.Weakness2}</b></td></tr>
            `;
        const attributesweaknessMV = document.getElementById('attributes-weaknessMV');
        attributesweaknessMV.innerHTML = `
                <tr>
                <td><img src="${data.Weakness.Weakness1Image}" alt="Weakness1"> </td>
                <td><b> ${data.Weakness.Weakness1}</b></td></tr>
                <tr>
                <td><img src="${data.Weakness.Weakness2Image}" alt="Weakness2"> </td>
                <td><b> ${data.Weakness.Weakness2}</b></td></tr>
            `;

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