const h=document.querySelector("title").textContent,E=`/public/data/${h}.json`;fetch(E).then(t=>t.json()).then(t=>{t.Name&&(document.getElementById("character-name").textContent=t.Name),t.Class&&(document.getElementById("class-name").textContent=t.Class),t.CharPortrait&&(document.getElementById("character-portrait").src=t.CharPortrait);const c=document.getElementById("attributes-body");c.innerHTML=`
            <tr><td>HP</td><td>${t.Attributes.HP}</td></tr>
            <tr><td>ATK</td><td>${t.Attributes.ATK}</td></tr>
            <tr><td>DEF</td><td>${t.Attributes.DEF}</td></tr>
            <tr><td>Stability Gauge</td><td>${t.Attributes.StabilityGauge}</td></tr>
            <tr><td>Movement Speed</td><td>${t.Attributes.MovementSpeed}</td></tr>
        `;function d(e){let s="";return e.SAtt1Image&&e.SAtt1&&(s+=`
                    <tr>
                        <td><img src="${e.SAtt1Image}" alt="Att1"> </td>
                        <td>${e.SAtt1}</td>
                    </tr>
                `),e.SAtt2Image&&e.SAtt2&&(s+=`
                    <tr>
                        <td><img src="${e.SAtt2Image}" alt="Att2"> </td>
                        <td>${e.SAtt2}</td>
                    </tr>
                `),s}const o=document.getElementById("attributes-type");o.innerHTML=d(t.SkillAttribute);const a=document.getElementById("attributes-typeMV");let m=d(t.SkillAttribute);a.innerHTML=m;function i(e){let s="";return e.Weakness1Image&&e.Weakness1&&(s+=`
                    <tr>
                        <td><img src="${e.Weakness1Image}" alt="Weakness1"> </td>
                        <td><b>${e.Weakness1}</b></td>
                    </tr>
                `),e.Weakness2Image&&e.Weakness2&&(s+=`
                    <tr>
                        <td><img src="${e.Weakness2Image}" alt="Weakness2"> </td>
                        <td><b>${e.Weakness2}</b></td>
                    </tr>
                `),s}const l=document.getElementById("attributes-weakness");l.innerHTML=i(t.Weakness);const g=document.getElementById("attributes-weaknessMV");let u=i(t.Weakness);g.innerHTML=u,document.getElementById("class-image-id").src=t.ClassImage,document.getElementById("class-image-idMV").src=t.ClassImage;const b=document.getElementById("effects-body");if(t.Effects&&t.Effects.Full){const e=t.Effects.Full.split(`

`);b.innerHTML=e.map(s=>{const[r,...n]=s.split(":"),$=n.join(":").trim();return`<tr><td><strong>${r}:</strong> ${$}</td></tr>`}).join("")}const f=document.getElementById("skills-info");[...t.Basic,...t.Skill,...t.Skill2,...t.Ultimate,...t.Passive].forEach(e=>{const s=Object.keys(e).filter(n=>(n.startsWith("Vertebrae")||n.startsWith("Fixed Key"))&&e[n]!==null);let r="";s.length>0&&(r=s.map(n=>`
                    <div class="mt-2">
                        <strong>${n}:</strong> ${e[n]}
                    </div>
                `).join("")),f.innerHTML+=`
                <div class="col">
                    <div class="card">
                        <div class="card-header d-flex align-items-center">
                            <img src="${e.SkillImage}" alt="Skill Image" class="skill-img">
                            ${e.SkillName||""}
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
                                            <td>${e.Range||"--"}</td>
                                            <td>${e.Att1||"--"}</td>
                                            <td>${e.Att2||"--"}</td>
                                            <td>${e.Att3||"--"}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="row">
                                <div class="col-4">
                                    <img src="${e.RangeImage}" alt="Range Image" class="img-fluid">
                                </div>
                                <div class="col-8 table-responsive">
                                    <p>${e.Description}</p>
                                </div>
                            </div>
                            ${r}
                        </div>
                    </div>
                </div>
            `});const I=document.getElementById("upgrades-body"),y=document.getElementById("upgrades-bodyMV");Object.keys(t.Upgrades).forEach(e=>{t.Upgrades[e].forEach(s=>{I.innerHTML+=`
                    <tr>
                        <td class="bg-dark text-center">
                            <img src="${s.IconImage}" alt="Icon" class="upgrade-icon">
                        </td>
                        <td>${e}</td>
                        <td><b>${s.SkillName}</b></td>
                        <td>${s.Effect.replace(/\n/g,"<br>")}</td>
                    </tr>
                `,y.innerHTML+=`
                    <tr>
                        <td class="bg-dark text-center">
                            <img src="${s.IconImage}" alt="Icon" class="upgrade-icon">
                        </td>
                        <td>${e}</td>
                        <td><b>${s.SkillName}</b></td>
                    </tr>
                    <tr>
                        <td colspan="3" class="effect-header">
                            Effect
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3">
                            ${s.Effect.replace(/\n/g,"<br>")}
                        </td>
                    </tr>
                `})})}).catch(t=>console.error("Error fetching JSON:",t));function p(t){document.getElementById("character-portrait").src=t,document.getElementById("character-imageMV").src=t}document.querySelectorAll(".btn-custom").forEach(t=>{t.addEventListener("click",function(){const c=this.getAttribute("data-image");p(c)})});
