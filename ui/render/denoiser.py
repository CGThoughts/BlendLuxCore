from bl_ui.properties_render import RenderButtonsPanel
from bpy.types import Panel
from ...utils.refresh_button import template_refresh_button
from ...engine.base import LuxCoreRenderEngine
from .. import icons
from ...properties.denoiser import LuxCoreDenoiser
from .icons import icon_manager


class LUXCORE_RENDER_PT_denoiser(RenderButtonsPanel, Panel):
    COMPAT_ENGINES = {"LUXCORE"}
    bl_label = "Intel Open Image Denoiser"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 60

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == "LUXCORE"

    def draw_header(self, context):
        layout = self.layout
        layout.enabled = not LuxCoreRenderEngine.final_running
        layout.prop(context.scene.luxcore.denoiser, "enabled", icon_value= icon_manager.get_icon_id("intel"))

    def draw(self, context):
        config = context.scene.luxcore.config
        denoiser = context.scene.luxcore.denoiser
        
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.active = denoiser.enabled

        sub = layout.column(align=True)
        # The user should not be able to request a refresh when denoiser is disabled
        sub.enabled = denoiser.enabled
        template_refresh_button(LuxCoreDenoiser.refresh, "luxcore.request_denoiser_refresh",
                                sub, "Running denoiser...")

        col = layout.column(align=True)
        col.enabled = denoiser.enabled and not LuxCoreRenderEngine.final_running

        if denoiser.type == "OIDN":
            sub = layout.column(align=False)
            sub.prop(denoiser, "max_memory_MB")
            sub.prop(denoiser, "albedo_specular_passthrough_mode")
            sub.prop(denoiser, "prefilter_AOVs")


class LUXCORE_RENDER_PT_denoiser_bcd_advanced(RenderButtonsPanel, Panel):
    COMPAT_ENGINES = {"LUXCORE"}
    bl_label = "Advanced"
    bl_parent_id = "LUXCORE_RENDER_PT_denoiser"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        denoiser = context.scene.luxcore.denoiser
        return context.scene.render.engine == "LUXCORE" and denoiser.type == "BCD"

    def draw(self, context):
        denoiser = context.scene.luxcore.denoiser
        
        layout = self.layout
        layout.enabled = denoiser.enabled and not LuxCoreRenderEngine.final_running

        layout.use_property_split = True
        layout.use_property_decorate = False
        
        layout.prop(denoiser, "scales")
        layout.prop(denoiser, "patch_radius")


