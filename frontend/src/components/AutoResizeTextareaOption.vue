<template>
  <div class="auto-resize-textarea-option">
    <label v-if="option.label">{{ option.label }}</label>
    <textarea
      v-model="option.value"
      @input="autoResize"
      :placeholder="option.placeholder || ''"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: 'AutoResizeTextareaOption',
  props: {
    option: {
      type: Object,
      required: true,
    },
  },
  methods: {
    autoResize(event) {
      const textarea = event.target;
      textarea.style.height = 'auto';
      textarea.style.height = `${textarea.scrollHeight}px`;
    },
  },
  mounted() {
    this.$nextTick(() => {
      const textarea = this.$el.querySelector('textarea');
      textarea.style.height = 'auto';
      textarea.style.height = `${textarea.scrollHeight}px`;
    });
  },
};
</script>

<style scoped>
.auto-resize-textarea-option textarea {
  width: 100%;
  min-height: 50px;
  resize: none;
  overflow-y: hidden;
}
</style>