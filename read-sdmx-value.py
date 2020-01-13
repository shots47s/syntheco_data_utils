import sys
import csv
import sdmx


def main():
    dataset_path = sys.argv[1]
    dsd_path = sys.argv[2]

    with open(dataset_path) as dataset_fileobj:
        with open(dsd_path) as dsd_fileobj:
            dataset_reader = sdmx.generic_data_message_reader(
                fileobj=dataset_fileobj,
                dsd_fileobj=dsd_fileobj,
            )
            _print_values(dataset_reader)


def _print_values(dataset_reader):
    for dataset in dataset_reader.datasets():
        key_family = dataset.key_family()
        name = key_family.name(lang="en")

        print name 

        dimension_names = key_family.describe_dimensions(lang="en") + ["Time", "Value"]

        print dimension_names
	count = 0
        
	## metadata file
        metadata_dict = {}
	for dim in key_family.describe_dimensions(lang="en"):
	    metadata_dict[dim] = {}

	for series in dataset.series():
	    key = series._series_key
	    key_desc = series.describe_key(lang="en")
	    for k,v in key_desc.items():
		# find this key
		ind = -1
		for kk,vv in key:
		    if vv == v:
			ind = kk
 			break
		if ind not in metadata_dict[k].keys():
		    metadata_dict[k][ind] = v

	
        print metadata_dict
	#with open("metadata.csv","w") as csv_file:
	#    cvs_write = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
	    		
	'''    
        with open("out.csv","w") as csv_file:
	    csv_write = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
	    csv_write.writerow(dimension_names)
	    for series in dataset.series():
                count += 1
                row_template = []
                key = series.describe_key(lang="en")
		row_template = [x[1] for x in series._series_key]
                #for key_name, key_value in key.items():
                #    row_template.append(key_value)

                for observation in series.observations(lang="en"):
                    row = row_template[:]
                    row.append(observation.time)
                    row.append(observation.value)

                    row_values = zip(dimension_names, row)
		    csv_write.writerow(row)
           '''         


main()
