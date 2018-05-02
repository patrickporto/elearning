<template>
    <div class="message-container">
        <div class="message-list">
            <div class="message-content" v-for="(msg, index) in messages" :key="index"
                :title="contentTitle">
                <div class="message-inside">
                    {{ msg.content }}
                </div>
            </div>
        </div>
        <img class="message-photo" :src="profileImg" />
    </div>
</template>

<script>
import moment from 'moment';

moment.locale('pt-BR');

export default {
    props: ['messages', 'profileImg'],
}
</script>

<style lang="sass">
    $background-color: #F7F7F7;

    .message {
        &-inside {
            background: $background-color;
            border-radius: 4px;
            display: inline-block;
            padding: 10px;
        }

        &-content {
            display: block;
            position: relative;
        }

        &-content + &-content {
            margin-top: 5px;
        }

        &-content + &-content:after {
            content: none;
        }

        &-list {
            display: inline-block;
        }

        &-container {
            text-align: right;
        }

        &-container + &-container {
            margin-top: 20px;
        }

        &-photo {
            border-radius: 100%;
            display: inline-block;
            max-width: 64px;
            vertical-align: top;
        }

        &-list + &-photo {
            margin-left: 10px;
        }

        &-content:after {
            left: 100%;
            top: 50%;
            border: solid transparent;
            content: " ";
            height: 0;
            width: 0;
            position: absolute;
            pointer-events: none;
            border-color: rgba(136, 183, 213, 0);
            border-left-color: $background-color;
            border-width: 10px;
            margin-top: -10px;
        }
    }
</style>
