<template>
    <v-container>
        <v-col cols="6">
            <div id="preview">
                <div v-html="text"></div>
            </div>
            <v-col>
                <v-btn
                color="indigo"
                v-on:click="copyText()"
                >
                    {{btn_text}}
                </v-btn>
            </v-col>
        </v-col>
    </v-container>
</template>

<style>
#preview {
    background-color:rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 3px;
}

code {
    background-color: transparent !important;
    padding: 0 !important;
}
</style>

<script>
import {marked} from 'marked';
export default {
    name: 'OutputText',
    props: ['formatted_text'],
    data: () => ({
        btn_text: "COPY",
    }),

    computed: {
        text() {
            let text = "```markdown \n" + this.formatted_text +  "```"

            return marked(text)
        }
    },
    watch: {
        'formatted_text': function() {
            this.btn_text = "COPY"
        }
    },
    methods: {
        copyText() {
            navigator.clipboard.writeText(this.formatted_text)
            .then(() => {
                this.btn_text = "COPIED!"
            })
            .catch(e => {
                console.error(e)
            })
        }
    }
}
</script>