from django import forms
from django.forms.forms import DeclarativeFieldsMetaclass, BaseForm
from django.forms.models import ModelFormMetaclass, BaseModelForm
from django.forms.utils import flatatt
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

LABEL_TEMPLATE = '<label {}>{}</label>'


class CustomLabelBoundField(forms.boundfield.BoundField):

    def label_tag(self, contents=None, attrs=None, label_suffix=None):
        """
        Wrap the given contents in a <label>, if the field has an ID attribute.
        contents should be mark_safe'd to avoid HTML escaping. If contents
        aren't given, use the field's HTML-escaped label.

        If attrs are given, use them as HTML attributes on the <label> tag.

        label_suffix overrides the form's label_suffix.
        """
        contents = contents or self.label
        if label_suffix is None:
            label_suffix = (self.field.label_suffix if self.field.label_suffix is not None
                            else self.form.label_suffix)
        # Only add the suffix if the label does not end in punctuation.
        # Translators: If found as last label character, these punctuation
        # characters will prevent the default label_suffix to be appended to the label
        if label_suffix and contents and contents[-1] not in _(':?.!'):
            contents = format_html('{}{}', contents, label_suffix)
        widget = self.field.widget
        id_ = widget.attrs.get('id') or self.auto_id
        if id_:
            id_for_label = widget.id_for_label(id_)
            attrs = {**(attrs or {}), 'class': 'form-label'}
            if id_for_label:
                attrs = {**(attrs or {}), 'for': id_for_label}
            if self.field.required and hasattr(self.form, 'required_css_class'):
                attrs = attrs or {}
                if 'class' in attrs:
                    attrs['class'] += ' ' + self.form.required_css_class
                else:
                    attrs['class'] = self.form.required_css_class
            attrs = flatatt(attrs) if attrs else 'aa'
            contents = format_html(LABEL_TEMPLATE, attrs, contents.replace(':', ''))
        else:
            contents = conditional_escape(contents)
        return mark_safe(contents)


def get_bound_field(field, form, field_name):
    """
    Return a BoundField instance that will be used when accessing the form
    field in a template.
    """
    return CustomLabelBoundField(form, field, field_name)


class XBaseModelForm(BaseModelForm):

    def as_tabler(self, margin_bottom='mb-3'):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<div class="'+margin_bottom+'"%(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="form-hint">%s</span>',
            errors_on_separate_row=True,
        )


class XModelForm(XBaseModelForm, metaclass=ModelFormMetaclass):
    pass


class XForm(BaseForm, metaclass=DeclarativeFieldsMetaclass):
    pass


class ModelLabelForm(XModelForm):
    required_css_class = 'required'

    def __getitem__(self, name):
        """Return a BoundField with the given name."""
        try:
            field = self.fields[name]
        except KeyError:
            raise KeyError(
                "Key '%s' not found in '%s'. Choices are: %s." % (
                    name,
                    self.__class__.__name__,
                    ', '.join(sorted(self.fields)),
                )
            )
        if name not in self._bound_fields_cache:
            self._bound_fields_cache[name] = get_bound_field(field, self, name)
        return self._bound_fields_cache[name]


class LabelForm(XForm):
    required_css_class = 'required'

    def __getitem__(self, name):
        """Return a BoundField with the given name."""
        try:
            field = self.fields[name]
        except KeyError:
            raise KeyError(
                "Key '%s' not found in '%s'. Choices are: %s." % (
                    name,
                    self.__class__.__name__,
                    ', '.join(sorted(self.fields)),
                )
            )
        if name not in self._bound_fields_cache:
            self._bound_fields_cache[name] = get_bound_field(field, self, name)
        return self._bound_fields_cache[name]
