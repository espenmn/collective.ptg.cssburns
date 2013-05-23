from collective.plonetruegallery.utils import createSettingsFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.plonetruegallery.browser.views.display import BaseDisplayType
from collective.plonetruegallery.interfaces import IBaseSettings
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.ptg.cssburns')

class ICssburnsDisplaySettings(IBaseSettings):
    cssburns_imagewidth = schema.Int(
        title=_(u"label_cssburns_imagewidth",
            default=u"Width of (each) image"),
        default=400,
        min=50)
    cssburns_imageheight = schema.Int(
        title=_(u"label_cssburns_imageheight",
            default=u"Height of (each) image"),
        default=260,
        min=50)
    cssburns_use_icons = schema.Bool(
        title=_(u"label_cssburns_use_icons",
            default=u"Use Thumbnail size instead of Size"),
        default=False)
    cssburns_downloadlink = schema.Bool(
        title=_(u"label_cssburns_downloadlink",
            default=u"Show download link"),
        default=False)
    cssburns_opacity = schema.Choice(
        title=_(u"label_cssburns_opacity",
                default=u"Opacity on mouse over"),
        default=0.3,
        vocabulary=SimpleVocabulary([
            SimpleTerm(0, 0,
                _(u"label_cssburns_opacity0",
                    default=u"0 Hide it completely")),
            SimpleTerm(0.1, 0.1,
                _(u"label_cssburns_opacity1",
                    default=u"0.1 Almost gone")),
            SimpleTerm(0.2, 0.2,
                _(u"label_cssburns_opacity2", default=u"0.2")),
            SimpleTerm(0.3, 0.3,
                _(u"label_cssburns_opacity3", default=u"0.3")),
            SimpleTerm(0.4, 0.4,
                _(u"label_cssburns_opacity4",
                    default=u"0.4 A bit more")),
            SimpleTerm(0.5, 0.5,
                _(u"label_cssburns_opacity5", default=u"0.5")),
            SimpleTerm(0.6, 0.6,
                _(u"label_cssburns_opacity6",
                    default=u"0.6")),
            SimpleTerm(0.7, 0.7,
                _(u"label_cssburns_opacity7",
                    default=u"0.7 Quite a bit")),
            SimpleTerm(0.8, 0.8,
                _(u"label_cssburns_opacity8",
                    default=u"0.8 A bit much")),
            SimpleTerm(0.9, 0.9,
                _(u"label_cssburns_opacity9",
                    default=u"0.9 Almost nothing")),
            SimpleTerm(1, 1,
                _(u"label_cssburns_opacity10",
                    default=u"1 Off")
            )
        ]))
    cssburns_toppadding = schema.TextLine(
        title=_(u"label_cssburns_toppadding",
            default=u"Padding above imagetitle"),
        default=u"90px")
    cssburns_bottompadding = schema.TextLine(
        title=_(u"label_cssburns_bottompadding",
            default=u"Padding below imagedescription"),
        default=u"70px")

class CssburnsDisplayType(BaseDisplayType):
    name = u"cssburns"
    schema = ICssburnsDisplaySettings
    description = _(u"label_cssburns_display_type",
        default=u"CSSburns")

    def javascript(self):
        return "" 

    def css(self):
        return u"""
<style>
#CSS3Slideshow .img3{
border: %(number_of_images)ipx solid black;
}
</style>
<link rel="stylesheet" type="text/css" href="++resource++ptg.cssburns/style.css"/>
""" % {
        'boxheight': self.settings.cssburns_imageheight,
        'boxwidth': self.settings.cssburns_imagewidth,
        'opacity': self.settings.cssburns_opacity,
        'bottompadding' : self.settings.cssburns_bottompadding,
        'toppadding' : self.settings.cssburns_toppadding,
        'number_of_images' : self.adapter.cooked_images,
       }

CssburnsSettings = createSettingsFactory(CssburnsDisplayType.schema)
