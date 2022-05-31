import requests
import datetime


class pbdb:
    def __init__(self, version=1.2):
        self.base_url = 'http://paleobiodb.org'
        self.version = 'data' + str(version)
        self.method = ''
        self.format = ''
        self.target_url = ''

    def make_kw(self, **kwargs):
        kw_part = []
        for para, values in kwargs.items():
            kw_part.append('%s=%s' % (str(para), str(values)))
        return '&'.join(kw_part)

    def make_fp(self):
        return '/'.join([self.base_url, self.version, self.method, self.format])

    def result_of_url(self):
        print(self.target_url)
        res = requests.get(url=self.target_url, headers={'user-agent': 'Mozilla 5.0'})
        res.encoding = res.apparent_encoding

        result_file = str(datetime.datetime.now()).replace(':', '-') + '.' + self.format
        with open(result_file, 'wb') as r:
            r.write(res.content)
            print('%s saved' % result_file)


class fossil_occurrences(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'occs'

    def single_fossil_occurrence(self, iformat='', **kwargs):
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def geographic_summary_of_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'geosum.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def taxonomy_of_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'taxa.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def fossil_diversity_over_time_full_computation(self, iformat='', **kwargs):
        self.format = 'diversity.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def fossil_diversity_over_time_quick_computation(self, iformat='', **kwargs):
        self.format = 'quickdiv.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def fossil_diversity_over_time_diagnostic(self, iformat='', **kwargs):
        self.format = 'checkdiv.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def most_prevalent_taxa(self, iformat='', **kwargs):
        self.format = 'prevalence.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def stratigraphy_of_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'strata.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def bibliographic_references_for_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def occurrences_grounded_by_bibliographic_reference(self, iformat='', **kwargs):
        self.format = 'byref.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def taxa_associated_with_fossil_occurrences_grounded_by_bibliographic_reference(self, iformat='', **kwargs):
        self.format = 'taxabyref.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def opinions_for_fossil_occurrences(self, iformat='', **kwargs):
        self.format = 'opinions.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class fossil_collections(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'colls'

    def single_fossil_collection(self, iformat='', **kwargs):
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_fossil_collections(self, iformat='', **kwargs):
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def geographic_summary_of_fossil_collections(self, iformat='', **kwargs):
        self.format = 'summary.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def bibliographic_references_for_fossil_collections(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def collections_grounded_by_bibliographic_reference(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class specimens_and_measurements(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'specs'

    def single_specimen(self, iformat='', **kwargs):
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_specimens(self, iformat='', **kwargs):
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class taxonomic_names(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'taxa'

    def single_taxon(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_taxa(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def opinions_about_taxa(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'opinions.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def taxonomy_of_fossil_occurrences(self, iformat='', **kwargs):
        self.method = 'occs'
        self.format = 'taxa.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def bibliographic_references_for_taxa(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'refs.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def taxa_grouped_by_bibliographic_reference(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'byref.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def auto_completion_for_taxonomic_names(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'auto.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def thumbnail_images_of_lifeforms(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'thumb.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def icon_images_of_lifeforms(self, iformat='', **kwargs):
        self.method = 'taxa'
        self.format = 'icon.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class taxonomic_opinions(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'opinions'

    def single_opinion(self, iformat='', **kwargs):
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_opinions(self, iformat='', **kwargs):
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class geological_time_intervals_and_time_scales(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'intervals'

    def single_geological_time_interval(self, iformat='', **kwargs):
        self.method = 'intervals'
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_geological_time_intervals(self, iformat='', **kwargs):
        self.method = 'intervals'
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def single_geological_time_scale(self, iformat='', **kwargs):
        self.format = 'single.%s' % iformat
        self.method = 'scales'
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_geological_time_scales(self, iformat='', **kwargs):
        self.method = 'scales'
        self.format = 'list.%s' % iformat
        self.result_of_url()


class geological_timescales_intervals_and_interval_bounds(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'timescales'

    def single_geological_timescale(self, iformat='', **kwargs):
        self.method = 'timescales'
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_geological_timescales(self, iformat='', **kwargs):
        self.method = 'timescales'
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def intervals_from_geological_timescales(self, iformat='', **kwargs):
        self.method = 'timescales'
        self.format = 'intervals.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def single_geological_time_interval(self, iformat='', **kwargs):
        self.method = 'intervals2'
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_geological_time_intervals(self, iformat='', **kwargs):
        self.method = 'intervals2'
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def add_timescales_or_updated_existing_timescales(self, iformat='', **kwargs):
        pass

    def define_intervals_from_timescale_bounds(self, iformat='', **kwargs):
        pass

    def remove_interval_definitions(self, iformat='', **kwargs):
        pass

    def delete_timescales(self, iformat='', **kwargs):
        pass

    def delete_interval_bounds(self, iformat='', **kwargs):
        pass


class geographic_places(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    pass


class geological_strata(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'strata'

    def list_of_geological_strata(self, iformat='', **kwargs):
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def auto_completion_for_geological_strata(self, iformat='', **kwargs):
        self.format = 'auto.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class bibliographic_references(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = 'refs'

    def single_bibliographic_reference(self, iformat='', **kwargs):
        self.method = 'refs'
        self.format = 'single.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def list_of_bibliographic_references(self, iformat='', **kwargs):
        self.method = 'refs'
        self.format = 'list.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def references_for_fossil_occurrences(self, iformat='', **kwargs):
        self.method = 'occs'
        self.format = 'refs.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def references_for_fossil_specimens(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.method = 'specs'
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def references_for_fossil_collections(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.method = 'colls'
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()

    def references_for_taxonomic_names(self, iformat='', **kwargs):
        self.format = 'refs.%s' % iformat
        self.method = 'taxa'
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class research_publications(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)
        self.method = ''

    def single_research_publication(self, iformat='', **kwargs):
        pass

    def list_of_research_publications(self, iformat='', **kwargs):
        pass

    def add_official_publications_or_update_existing_records(self, iformat='', **kwargs):
        pass

    def delete_official_publications(self, iformat='', **kwargs):
        pass


class data_archives(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    def single_data_archive(self, iformat='', **kwargs):
        pass

    def content_of_a_data_archive(self, iformat='', **kwargs):
        pass

    def list_of_data_archives(self, iformat='', **kwargs):
        pass

    def list_of_public_data_archives(self, iformat='', **kwargs):
        pass

    def add_data_archive_records_or_update_existing_records(self, iformat='', **kwargs):
        pass

    def delete_data_archives(self, iformat='', **kwargs):
        pass


class client_configuration(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    def client_configure(self, iformat='', **kwargs):
        self.format = 'config.%s' % iformat
        self.target_url = self.make_fp() + '?' + self.make_kw(**kwargs)
        self.result_of_url()


class combined_data(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    pass


class database_contributors():
    pass


class support_for_frontend_application(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    def save_or_retrieve_navigator_application_state(self, iformat='', **kwargs):
        pass


class database_statistics(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    def statistics_for_the_fronted_website(self, iformat='', **kwargs):
        pass


class educational_resources(pbdb):
    def __init__(self):
        pbdb.__init__(self, version=1.2)

    def add_educational_resources_or_update_existing_records(self, iformat='', **kwargs):
        pass

    def update_existing_educational_resource_records(self, iformat='', **kwargs):
        pass

    def delete_educational_resources(self, iformat='', **kwargs):
        pass


if __name__ == '__main__':
    fossil_occurrences = fossil_occurrences()
    fossil_collections = fossil_collections()
    specimens_and_measurements = specimens_and_measurements()
    taxonomic_names = taxonomic_names()
    taxonomic_opinions = taxonomic_opinions()
    geological_time_intervals_and_time_scales = geological_time_intervals_and_time_scales()
    geological_timescales_intervals_and_interval_bounds = geological_timescales_intervals_and_interval_bounds()
    geographic_places = geographic_places()
    geological_strata = geological_strata()
    bibliographic_references = bibliographic_references()
    research_publications = research_publications()
    data_archives = data_archives()
    client_configuration = client_configuration()
    combined_data = combined_data()
    database_contributors = database_contributors()
    support_for_frontend_application = support_for_frontend_application()
    database_statistics = database_statistics()
    educational_resources = educational_resources()
