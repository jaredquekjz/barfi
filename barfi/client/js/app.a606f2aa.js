(function(e){function t(t){for(var n,i,r=t[0],l=t[1],c=t[2],u=0,m=[];u<r.length;u++)i=r[u],Object.prototype.hasOwnProperty.call(o,i)&&o[i]&&m.push(o[i][0]),o[i]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(e[n]=l[n]);d&&d(t);while(m.length)m.shift()();return s.push.apply(s,c||[]),a()}function a(){for(var e,t=0;t<s.length;t++){for(var a=s[t],n=!0,r=1;r<a.length;r++){var l=a[r];0!==o[l]&&(n=!1)}n&&(s.splice(t--,1),e=i(i.s=a[0]))}return e}var n={},o={app:0},s=[];function i(t){if(n[t])return n[t].exports;var a=n[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=e,i.c=n,i.d=function(e,t,a){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)i.d(a,n,function(t){return e[t]}.bind(null,n));return a},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],l=r.push.bind(r);r.push=t,r=r.slice();for(var c=0;c<r.length;c++)t(r[c]);var d=l;s.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("cd49")},"856e":function(e,t,a){"use strict";a("a0c5")},9194:function(e,t,a){"use strict";a("b544")},a0c5:function(e,t,a){},a347:function(e,t,a){},b0f9:function(e,t,a){},b544:function(e,t,a){},c352:function(e,t,a){"use strict";a("b0f9")},cd49:function(e,t,a){"use strict";a.r(t);var n=a("2b0e"),o=function(){var e=this,t=e._self._c;return t("div",{attrs:{id:"app"}},[t("WithStreamlitConnection",{scopedSlots:e._u([{key:"default",fn:function({args:e}){return[t("block-editor",{attrs:{args:e}})]}}])})],1)},s=[],i=function(){var e=this,t=e._self._c;e._self._setupProxy;return t("div",[""!=e.componentError?t("div",[t("h1",{staticClass:"err__title"},[e._v("Component Error")]),t("div",{staticClass:"err__msg"},[e._v(e._s(e.componentError))])]):void 0!=e.renderData?e._t("default",null,{args:e.renderData.args,disabled:e.renderData.disabled}):e._e()],2)},r=[],l=a("d092"),c=n["default"].extend({name:"withStreamlitConnection",data:()=>({renderData:void 0,componentError:""}),methods:{onRenderEvent:function(e){const t=e;this.renderData=t.detail,this.componentError=""}},mounted(){l["a"].events.addEventListener(l["a"].RENDER_EVENT,this.onRenderEvent),l["a"].setComponentReady(),l["a"].setFrameHeight()},updated(){l["a"].setFrameHeight()},destroyed(){l["a"].events.removeEventListener(l["a"].RENDER_EVENT,this.onRenderEvent)},errorCaptured(e){this.componentError=String(e)}}),d=c,u=(a("9194"),a("2877")),m=Object(u["a"])(d,i,r,!1,null,"42636045",null),h=m.exports,p=function(){var e=this,t=e._self._c;return t("div",{attrs:{id:"editorCanvas"}},[t("div",{staticClass:"modal",style:e.menuModal?"display: block;":"display: none;"},[t("div",{staticClass:"modal-content"},[t("span",{staticClass:"close",on:{click:function(t){e.menuModal=!e.menuModal}}},[e._v("×")]),t("div",{staticClass:"tab"},[t("button",{staticClass:"tablinks",class:e.listTab?"active":"",on:{click:function(t){return e.activateTab("listTab")}}},[e._v(" List ")]),t("button",{staticClass:"tablinks",class:e.saveTab?"active":"",on:{click:function(t){return e.activateTab("saveTab")}}},[e._v(" Save ")])]),t("div",{staticClass:"tabcontent",style:e.listTab?"display: block;":"display: none;"},[t("label",[e._v("List of saved schemas")]),t("ul",e._l(e.loadSchemas,(function(a,n){return t("li",{key:n},[e._v(" "+e._s(a)+" ")])})),0),t("p",[e._v(" Current schema: "),t("span",{staticStyle:{"font-weight":"600"}},[e._v(e._s(this.loadSchemaName))])])]),t("div",{staticClass:"tabcontent",style:e.saveTab?"display: block;":"display: none;"},[t("label",[e._v("Enter name to save schema as")]),t("input",{directives:[{name:"model",rawName:"v-model",value:e.saveSchemaName,expression:"saveSchemaName"}],attrs:{placeholder:"Schema name"},domProps:{value:e.saveSchemaName},on:{input:function(t){t.target.composing||(e.saveSchemaName=t.target.value)}}}),""!==e.saveSchemaName?t("button",{staticClass:"modal-button",on:{click:e.saveEditorData}},[e._v(" Save ")]):t("button",{staticClass:"modal-button modal-button-disabled",on:{click:e.saveEditorData}},[e._v(" Save ")]),this.saveSchemaName===this.loadSchemaName?t("p",[e._v(" The entered schema name is similar to one already existing in the database, saving will override the data for the schema name. ")]):e._e()])])]),t("baklava-editor",{attrs:{plugin:e.viewPlugin}}),t("div",{staticClass:"button-menu"},[t("button",{on:{click:function(t){e.menuModal=!e.menuModal}}},[e._v("Menu")]),t("button",{on:{click:e.executeEditorData}},[e._v("Convert")])])],1)},v=[],f=(a("0643"),a("4e3e"),a("dac5")),b=a("0c30"),_=a("9f16"),g=a("0048");function y({BlockName:e,Inputs:t,Outputs:a,Options:n}){const o=new f["NodeBuilder"](e);return o.setName(e),t.forEach(e=>{o.addInputInterface(e.name,e.type,e.value,e.properties)}),a.forEach(e=>{o.addOutputInterface(e.name,e.type,e.value,e.properties)}),n.forEach(e=>{o.addOption(e.name,e.type,e.value,e.sidebar,e.properties)}),o.build()}var k={name:"BlockEditor",props:["args"],data(){return{editor:new f["Editor"],viewPlugin:new b["ViewPlugin"],engine:new g["Engine"](!0),menuModal:!1,listTab:!0,saveTab:!1,saveSchemaName:"",loadSchemaName:"",loadSchemas:[],BlockNameID:{}}},created(){this.loadSchemas=this.args.load_schema_names,this.editor.use(this.viewPlugin),this.editor.use(new _["OptionPlugin"]),this.editor.use(this.engine),this.viewPlugin.enableMinimap=!0,console.log(this.args),this.args.base_blocks.forEach(e=>{const t=y({BlockName:e.name,Inputs:e.inputs,Outputs:e.outputs,Options:e.options});Object.prototype.hasOwnProperty.call(e,"category")?this.editor.registerNodeType(e.name,t,e.category):this.editor.registerNodeType(e.name,t)}),this.args.load_editor_schema?(this.editor.load(this.args.load_editor_schema),this.updateBlockNameIDCounters()):this.args.base_blocks.forEach(e=>{this.BlockNameID[e.name]=1}),this.loadSchemaName=this.args.load_schema_name,this.editor.events.addNode.addListener(this,e=>{this.editor.nodes.forEach(t=>{t.id===e.id&&"Curriculum"!==t.name&&(t.name=t.name+"-"+this.BlockNameID[e.name]++)})})},methods:{executeEditorData(){l["a"].setComponentValue({command:"execute",editor_state:this.editor.save()})},saveEditorData(){l["a"].setComponentValue({command:"save",schema_name:this.saveSchemaName,editor_state:this.editor.save()}),this.saveSchemaName="",this.menuModal=!this.menuModal},activateTab(e){"listTab"===e&&(this.listTab=!0,this.saveTab=!1),"saveTab"===e&&(this.listTab=!1,this.saveTab=!0)},updateBlockNameIDCounters(){this.BlockNameID={},this.editor.nodes.forEach(e=>{if("Curriculum"===e.name)return;const t=e.name.match(/^(.*?)-(\d+)$/);if(t){const e=t[1],a=parseInt(t[2]);(!this.BlockNameID[e]||this.BlockNameID[e]<=a)&&(this.BlockNameID[e]=a+1)}else this.BlockNameID[e.name]||(this.BlockNameID[e.name]=2)}),this.args.base_blocks.forEach(e=>{this.BlockNameID[e.name]||(this.BlockNameID[e.name]=1)}),console.log("Updated BlockNameID:",this.BlockNameID)}}},N=k,E=(a("856e"),Object(u["a"])(N,p,v,!1,null,null,null)),S=E.exports,C={name:"App",components:{WithStreamlitConnection:h,BlockEditor:S}},D=C,w=(a("c352"),Object(u["a"])(D,o,s,!1,null,null,null)),T=w.exports;a("a347");n["default"].use(b["BaklavaVuePlugin"]),n["default"].config.productionTip=!1,n["default"].config.devtools=!1,n["default"].prototype.log=console.log,new n["default"]({render:e=>e(T)}).$mount("#app")}});
//# sourceMappingURL=app.a606f2aa.js.map